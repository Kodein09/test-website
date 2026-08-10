from pydantic import BaseModel, Field, EmailStr

class UserRegistrationSchema(BaseModel):
    name: str = Field(min_length=2, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8, max_length=100, max_digits=100)

class UserLoginSchema(BaseModel):
    email: EmailStr
    password: str = Field(min_length=8, max_length=100, max_digits=100)