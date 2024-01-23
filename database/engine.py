import motor.motor_asyncio

MONGODB_URL = "mongodb+srv://admin:admin@cluster0.altllj0.mongodb.net/?retryWrites=true&w=majority"
client = motor.motor_asyncio.AsyncIOMotorClient(MONGODB_URL)

db = client.python_db
collection_name = db["Users"]
