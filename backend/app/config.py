from pydantic import BaseModel
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseModel):
    app_name: str = "Enterprise Long-Term Memory Research Assistant"
    environment: str = os.getenv("ENVIRONMENT", "local")
    memory_backend: str = os.getenv("MEMORY_BACKEND", "local_json")  # later: cosmos/sql
    data_dir: str = os.getenv("DATA_DIR", ".data")

settings = Settings()
