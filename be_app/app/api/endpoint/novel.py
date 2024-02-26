from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter

from app.db.database import get_db

route = APIRouter()


@route.get("/api/novel")
async def get_novel():
    return {"message": "Hello World Novel"}