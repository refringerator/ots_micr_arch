from sqlalchemy import Column, Integer, String
from api.db import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(256))
    email = Column(String(50))
    first_name = Column(String)
    last_name = Column(String)
    phone = Column(String(50))

    def __init__(self, username, email, first_name, last_name, phone, *args, **kwargs):
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

    def data_update(self, *args, **kwargs):
        print(kwargs)
        for attr, value in kwargs.items():
            if hasattr(self, attr):
                setattr(self, attr, value)
