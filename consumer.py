from kafka import KafkaConsumer
from pymongo import MongoClient
import json
from datetime import datetime, timezone


# =========================================================
# CONFIGURATION
# =========================================================

KAFKA_SERVER = "localhost:9092"
TOPIC_NAME = "a1-data"

# USE THE SAME WORKING URI FROM test_mongo.py
MONGO_URI = "mongodb+srv://mongoadmin:mongoadmin005@abhi1.jkaywff.mongodb.net/"

DATABASE_NAME = "sda_course"
COLLECTION_NAME = "streamed_transactions"


# =========================================================
# MONGODB CONNECTION
# =========================================================

print("Connecting to MongoDB Atlas...")

client = MongoClient(
    MONGO_URI,
    serverSelectionTimeoutMS=10000
)

# Test authentication
client.admin.command("ping")

print("MongoDB Atlas connection successful!")

db = client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

print(f"Database     : {DATABASE_NAME}")
print(f"Collection   : {COLLECTION_NAME}")


# =========================================================
# KAFKA CONSUMER
# =========================================================

consumer = KafkaConsumer(
    TOPIC_NAME,
    bootstrap_servers=[KAFKA_SERVER],
    auto_offset_reset="earliest",
    group_id="mongodb-consumer",
    value_deserializer=lambda x: json.loads(
        x.decode("utf-8")
    )
)

print("Kafka consumer started!")
print(f"Listening on : {TOPIC_NAME}")
print("-" * 60)


# =========================================================
# CONSUME DATA AND STORE IN MONGODB
# =========================================================

count = 0

for msg in consumer:

    data = msg.value

    data["ingested_at"] = datetime.now(timezone.utc)

    collection.insert_one(data)

    count += 1

    print(
        f"[{count:04d}] "
        f"Stored transaction: "
        f"{data.get('transaction_id', 'Unknown')}"
    )