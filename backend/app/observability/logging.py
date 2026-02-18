import logging
import uuid

LOG_FORMAT = "%(asctime)s | %(levelname)s | %(name)s | request_id=%(request_id)s | %(message)s"

class RequestIdFilter(logging.Filter):
    def __init__(self):
        super().__init__()
        self.request_id = "unknown"

    def set(self, request_id: str):
        self.request_id = request_id

    def filter(self, record: logging.LogRecord) -> bool:
        record.request_id = self.request_id
        return True

request_id_filter = RequestIdFilter()

def setup_logging() -> logging.Logger:
    logger = logging.getLogger("enterprise_assistant")
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    handler.setFormatter(logging.Formatter(LOG_FORMAT))
    handler.addFilter(request_id_filter)

    if not logger.handlers:
        logger.addHandler(handler)

    return logger

def new_request_id() -> str:
    return str(uuid.uuid4())[:8]
