from typing import Optional

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from . import models


async def new_user_register(request, database: Session) -> models.User:
    new_user = models.User(
        username=request.username,
        email=request.email,
        first_name=request.first_name,
        last_name=request.last_name,
        phone=request.phone,
    )
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user


async def get_user_by_id(user_id, database: Session) -> Optional[models.User]:
    user_info = database.query(models.User).get(user_id)
    if not user_info:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Data Not Found!")
    return user_info


async def delete_user_by_id(user_id, database: Session):
    database.query(models.User).filter(models.User.id == user_id).delete()
    database.commit()
