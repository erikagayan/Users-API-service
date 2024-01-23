def individual_serial(users) -> dict:
    return {
        "id": str(users["_id"]),
        "username": users["username"],
        "email": users["email"],
        "first_name": users["first_name"],
        "last_name": users["last_name"]
    }


async def list_serial(users):
    return [individual_serial(user) async for user in users]
