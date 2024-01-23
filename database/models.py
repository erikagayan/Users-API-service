from pydantic import BaseModel


class Users(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
