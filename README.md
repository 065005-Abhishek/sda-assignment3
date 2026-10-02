\# SDA Assignment 3 - Streaming Data Analytics



\## Project Overview



This project demonstrates a streaming data analytics pipeline using Apache Kafka, Python, MongoDB Atlas and MongoDB Atlas Charts.



Transaction data from the sample dataset is published to the Kafka topic `a1-data`. The Python consumer reads the streamed transactions and stores them in MongoDB Atlas. MongoDB Atlas Charts is then used to visualize the consumed transaction data.



\## Technology Stack



\- Python

\- Apache Kafka

\- Zookeeper

\- MongoDB Atlas

\- MongoDB Atlas Charts

\- Docker



\## Data Flow



Sample Transaction Dataset

&#x20;       ↓

Kafka Producer

&#x20;       ↓

Kafka Topic: a1-data

&#x20;       ↓

consumer.py

&#x20;       ↓

MongoDB Atlas

&#x20;       ↓

Database: sda\_course

&#x20;       ↓

Collection: streamed\_transactions

&#x20;       ↓

MongoDB Atlas Charts



\## Kafka Topic



The Kafka topic used for this assignment is:



`a1-data`



\## Consumer



The `consumer.py` program:



1\. Connects to the Kafka broker.

2\. Subscribes to the `a1-data` topic.

3\. Consumes transaction messages.

4\. Decodes the transaction data.

5\. Adds an ingestion timestamp.

6\. Stores each transaction in MongoDB Atlas.

7\. Displays the consumed transaction count.



\## MongoDB Storage



Database:



`sda\_course`



Collection:



`streamed\_transactions`



\## Dashboard



The dashboard has been created using MongoDB Atlas Charts.



\### 1. Total Units Sold by Category



Grouped bar chart showing the total quantity of products sold across each category.



\### 2. Transactions by Payment Method



Donut chart showing the distribution of transactions across UPI, Credit Card and Debit Card.



\### 3. Top 10 Products by Units Sold



Grouped bar chart showing the top 10 products ranked according to total quantity sold.



\## Business Insights



The dashboard provides an overview of transaction volume across product categories, payment methods and individual products.



Electronics records approximately twice the unit sales volume of Home Appliances in the sample dataset.



UPI represents the largest share of transactions among the observed payment methods, followed by Credit Card and Debit Card.



At the product level, Headphones have the highest unit sales, followed by Smartwatch and Smartphone.



These visualizations demonstrate how streamed transaction data can be transformed into business insights related to category performance, payment behavior and product demand.



\## How to Run



\### 1. Start Kafka and Zookeeper



Start the Kafka and Zookeeper services using Docker.



\### 2. Start the Kafka Producer



Run:



```bash

py producera2.py

