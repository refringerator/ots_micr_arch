from . import models


async def new_user_register(request, database) -> models.User:
    new_user = models.User(username=request.username, email=request.email, firstName=request.firstName)
    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user

