from fastapi import FastAPI
from .observability.logging import setup_logging, new_request_id, request_id_filter
from .api.routes_chat import router as chat_router
from .api.routes_memory import router as memory_router
from .config import settings

logger = setup_logging()

app = FastAPI(title=settings.app_name)

@app.middleware("http")
async def add_request_id(request, call_next):
    rid = new_request_id()
    request_id_filter.set(rid)
    logger.info(f"{request.method} {request.url.path}")
    response = await call_next(request)
    response.headers["x-request-id"] = rid
    return response

app.include_router(chat_router, tags=["chat"])
app.include_router(memory_router, tags=["memory"])

@app.get("/health")
def health():
    return {"status": "ok", "app": settings.app_name}
