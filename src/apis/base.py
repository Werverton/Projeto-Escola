#aqui devem ser inseridas as rotas que serão expostas para o main.py

from apis.version1 import route_hello
from apis.version1 import route_schools
from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(route_hello.router, prefix="", tags=["hello"])
api_router.include_router(route_schools.router, prefix="/schools", tags=["schools"])