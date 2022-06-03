from fastapi import APIRouter
from core.config import settings

#app = FastAPI(title=settings.PROJECT_NAME,version=settings.PROJECT_VERSION)

router = APIRouter()

@router.get("/")
def hello_api():
    return {"msg":"Hello API"}