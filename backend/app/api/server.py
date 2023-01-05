from fastapi import FastAPI, APIRouter

from app.api.routers import images


def get_application():
    app = FastAPI()
    router = APIRouter()
    router.include_router(images.router, prefix="/images")
    app.include_router(router)
    return app


app = get_application()
