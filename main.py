from fastapi import FastAPI
from routers import get_users, get_user_by_id, post_users, update_users, delete_users

app = FastAPI()

app.include_router(get_users.router)
app.include_router(get_user_by_id.router)
app.include_router(post_users.router)
app.include_router(update_users.router)
app.include_router(delete_users.router)
