from pydantic import BaseModel


class Users(BaseModel):
    username: str
    first_name: str
    last_name: str
