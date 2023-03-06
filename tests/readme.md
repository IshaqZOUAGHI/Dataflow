pip3 install paho-mqtt python-etcd
pip3 install pykafka
python3 mqttbroker.py
kafka/bin/zookeeper-server-start.sh -daemon kafka/config/zookeeper.properties 
kafka/bin/kafka-server-start.sh -daemon kafka/config/server.properties 
python3 mqttkafka.py
kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 -topic temperature2