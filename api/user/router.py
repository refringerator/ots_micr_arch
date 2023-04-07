from fastapi import APIRouter, Depends, status, Response, HTTPException

from sqlalchemy.orm import Session

from api import db
from . import schema
from . import validator
from . import services

router = APIRouter(tags=['Users'], prefix='/user')


@router.post('/', status_code=status.HTTP_201_CREATED)
async def create_user_registration(request: schema.User, database: Session = Depends(db.get_db)):
    user = await validator.verify_email_exist(request.email, database)

    if user:
        raise HTTPException(status_code=400, detail="The user with this email already exist.")

    new_user = await services.new_user_register(request, database)
    return new_user



