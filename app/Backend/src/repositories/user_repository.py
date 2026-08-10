from pydantic import EmailStr
from uuid import UUID


class UserRepository:
    @staticmethod
    async def get_user_by_id(user_id: str):
        pass

    @staticmethod
    async def get_user_by_email(email: EmailStr):
        pass

    @staticmethod
    async def create_user(user_id: UUID, name: str, email, password: str):
        pass

    @staticmethod
    async def delete_user_by_id(user_id: str):
        pass