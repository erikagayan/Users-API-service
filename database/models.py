from pydantic import BaseModel, Field, EmailStr, field_validator


class Users(BaseModel):
    username: str = Field(..., max_length=20)
    email: EmailStr
    first_name: str
    last_name: str

    @field_validator("first_name", "last_name", mode="before")
    def capitalize_name(cls, value: str):
        return value.capitalize() if value else value
