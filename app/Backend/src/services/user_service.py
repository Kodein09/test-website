from uuid import uuid4
from argon2 import PasswordHasher

from ..repositories.user_repository import UserRepository
from ..schemas.user_schema import UserRegistrationSchema

ph = PasswordHasher(
    time_cost=3,
    memory_cost=65536
)

class UserService:
    @staticmethod
    async def reg_service(user_data: UserRegistrationSchema) -> dict:
        user_id = uuid4()
        hashed_password = ph.hash(user_data.password)
        await UserRepository.create_user(user_id, user_data.name, user_data.email, hashed_password)

        return {
            "name": user_data.name,
            "email": user_data.email
        }