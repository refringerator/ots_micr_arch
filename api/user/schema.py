from pydantic import BaseModel, constr, EmailStr


class User(BaseModel):
    username: constr(max_length=256)
    firstName: str
    email: EmailStr


