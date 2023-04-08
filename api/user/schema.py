from pydantic import BaseModel, constr, EmailStr, Field
from sqlalchemy import alias


class User(BaseModel):
    username: constr(max_length=256)
    first_name: str = Field(alias="firstName")
    last_name: str = Field(alias="lastName")
    email: EmailStr
    phone: str


class DisplayUser(User):
    id: int

    class Config:
        allow_population_by_field_name = True
        orm_mode = True
