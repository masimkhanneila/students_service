from fastapi import FastAPI

from app.controllers.student import router
from app.model.student import initialize_db

initialize_db()
app = FastAPI()
app.include_router(router)
