from datetime import datetime
import email
from os import access
from typing import Optional
import pydantic


from pydantic import BaseModel, EmailStr, conint

from app.database import Base
from app.models import User
    
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass



# class PostUpdate(PostBase):

class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    class Config:
        orm_mode = True

class PostResponse(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    class Config:
        orm_mode = True

class PostOut(BaseModel):
    Post: PostResponse
    votes:int

    class Config:
        orm_mode = True
    

class UserCreate(BaseModel):
    email: EmailStr
    password: str




class UserLogin(BaseModel):
    email : EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type : str

class TokenData(BaseModel):
    id: Optional[str]


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)