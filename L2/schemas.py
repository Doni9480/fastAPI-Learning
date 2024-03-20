"""
"""

from typing import List
from pydantic import BaseModel



class BaseAddress(BaseModel):
    """
    hello
    """
    id: int
    email_address: str
    user_id: int
    user: List["CreateUser"]


class CreateAddress(BaseAddress):
    pass


class AddressSchema(BaseAddress):
    id: int


class BaseUser(BaseModel):
    name: str
    fullname: str
    addresses: List["CreateAddress"]


class CreateUser(BaseUser):
    pass


class UserSchema(BaseUser):
    id: int
