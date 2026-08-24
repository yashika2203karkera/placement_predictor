import pandas as pd
import json
from pymongo import MongoClient

# Load CSV
df = pd.read_csv("data/placement.csv")

# Convert to JSON
json_data = json.loads(df.to_json(orient='records'))

# Connect MongoDB (make sure MongoDB is running)
client = MongoClient("mongodb://localhost:27017/")  # replace if using Atlas
db = client['placement_db']
collection = db['students']

# Insert data
collection.insert_many(json_data)
print("Data inserted into MongoDB")