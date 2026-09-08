from fastapi import FastAPI

from app.controllers.student import router

app = FastAPI()
app.include_router(router)
