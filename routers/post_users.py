from fastapi import APIRouter
from database.models import Users
from database.engine import collection_name


router = APIRouter()


"""POST Request Method"""


@router.post("/")
async def post_users(users: Users):
    await collection_name.insert_one(users.dict())
