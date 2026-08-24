from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

# Replace with your connection string (Local or MongoDB Atlas)
MONGO_URI = "mongodb://localhost:27017/" 
# For MongoDB Atlas: "mongodb+srv://<username>:<password>@cluster0.xxx.mongodb.net/"

try:
    # 1. Create client (set a 5-second timeout so it doesn't hang)
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    
    # 2. Send a ping to the admin database to verify the connection
    client.admin.command('ping')
    
    print("SUCCESS: Connected to MongoDB successfully!")

except ConnectionFailure:
    print("ERROR: Could not connect to MongoDB. Is the server running?")
except Exception as e:
    print(f"ERROR: An error occurred: {e}")