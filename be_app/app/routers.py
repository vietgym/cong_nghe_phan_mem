from fastapi import APIRouter

from app.api.endpoint import user, novel

router = APIRouter()

router.include_router(user.route, tags=["bgt"])
router.include_router(novel.route, tags=["novels"])