from fastapi import FastAPI
from routers.items import items_router
from routers.clockin import clockin_router

app = FastAPI()

app.include_router(
    items_router, 
    prefix="/items",
    tags=["Items"]
)

app.include_router(
    clockin_router, 
    prefix="/clock-in",
    tags=["Clock In"]
)
