from fastapi import APIRouter, status

from ..services.user_service import UserService
from ..schemas.user_schema import UserRegistrationSchema
from ..repositories.user_repository import UserRepository

router = APIRouter()

@router.post("/registration", status_code=status.HTTP_409_CONFLICT)
async def registration(user_data: UserRegistrationSchema) -> dict:
    user_exist = UserRepository.get_user_by_email(user_data.email)
    if user_exist:
        raise status.HTTP_409_CONFLICT

    created_user = UserService.reg_service(user_data)
    return {
        "info": created_user
    }
