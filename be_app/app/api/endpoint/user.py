from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, APIRouter

from app.db.database import get_db

route = APIRouter()


@route.get("/api/user")
async def get_users():
    return {"message": "Hello World User"}