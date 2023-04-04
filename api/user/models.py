from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from api.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(256))
    email = Column(String(50))
    firstName = Column(String)

    def __init__(self, username, email, firstName, *args, **kwargs):
        self.username = username
        self.email = email
        self.firstName = firstName
