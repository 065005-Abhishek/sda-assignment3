import csv
import json
import time
from kafka import KafkaProducer

# Kafka configuration
KAFKA_SERVER = "localhost:9092"
TOPIC_NAME = "a1-data"

# Create Kafka producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

print("Kafka Producer Started...")
print(f"Streaming data to topic: {TOPIC_NAME}")
print("-" * 50)

# Read CSV file
with open("sample_data.csv", mode="r", encoding="utf-8") as file:

    reader = csv.DictReader(file)

    for row in reader:

        # Convert numerical values
        row["price"] = float(row["price"])
        row["quantity"] = int(row["quantity"])

        # Send record to Kafka
        producer.send(TOPIC_NAME, value=row)

        print("Sent:", row)

        # Wait 2 seconds between messages
        time.sleep(2)

# Make sure all messages are delivered
producer.flush()

print("-" * 50)
print("All messages have been sent successfully.")