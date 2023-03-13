

#!/bin/bash

# Install Java JDK
sudo apt-get update -y
sudo apt-get install -y default-jdk

# Download and install Kafka
curl -sSOL https://downloads.apache.org/kafka/3.4.0/kafka_2.13-3.4.0.tgz
tar -xzf kafka_2.13-3.4.0.tgz
mv kafka_2.13-3.4.0 kafka

./kafka/bin/zookeeper-server-start.sh -daemon ./kafka/config/zookeeper.properties
./kafka/bin/kafka-server-start.sh -daemon ./kafka/config/server.properties

echo "Waiting for 10 secs until kafka and zookeeper services are up and running"
sleep 10

ps -ef | grep kafka
# Create a Kafka topic for car data
./kafka/bin/kafka-topics.sh --create --bootstrap-server 127.0.0.1:9092 --replication-factor 1 --partitions 1 --topic car-data


./kafka/bin/kafka-topics.sh --describe --bootstrap-server 127.0.0.1:9092 --topic car-data
