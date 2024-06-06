from fastapi import APIRouter
from controllers import auth_controller, user_controller

router = APIRouter()

router.include_router(auth_controller.router, tags=["authorization"])
router.include_router(user_controller.router, prefix="/users", tags=["users"])
