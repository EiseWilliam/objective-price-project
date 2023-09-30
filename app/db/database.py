from motor.motor_asyncio import AsyncIOMotorClient

# client = AsyncIOMotorClient(settings.DATABASE_URL)


# client = AsyncIOMotorClient("mongodb://localhost:27017/")


# try:
#     conn = client.server_info()
#     print(f'Connected to MongoDB {conn.get("version")}')
# except Exception:
#     print("Unable to connect to the MongoDB server.")

# db = client.get_database("Pricely")
# User = db.get_collection("users")
# History = db.get_collection("history")


# logger = logging.getLogger(__name__)

# def connect_to_mongodb():
#     try:
#         # Use settings to get the MongoDB URL and database name
#         conn = client.server_info()
#         logger.info(f'Connected to MongoDB')
#         return client.get_database("Pricely")
#     except Exception as e:
#         logger.error(f"Unable to connect to the MongoDB server: {e}")
#         raise

# Usage:
client = AsyncIOMotorClient("mongodb://localhost:27017/")
db = client["Pricely"]
User = db["users"]
History = db["histories"]
