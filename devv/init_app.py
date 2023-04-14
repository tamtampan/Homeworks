from fastapi import FastAPI
from beverages import beverage_router
from device_models import device_model_router


def init_app():
    app = FastAPI()
    app.include_router(beverage_router)
    app.include_router(device_model_router)
    return app


app = init_app()
