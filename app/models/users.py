from pydantic import BaseModel, EmailStr

class UserBase(BaseModel):
    username: str
    email: EmailStr


class UserInDB(UserBase):
    hashed_password: str


class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str
