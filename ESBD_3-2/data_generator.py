import json
import random
import time
from uuid import uuid4

import pandas as pd
from confluent_kafka import Producer

# set up Kafka producer
TOPIC = "creditcard_transactions"
producer = Producer({"bootstrap.servers": "localhost:9092"})


def main():
    csv_data = pd.read_csv("creditcard.csv")
    csv_data.drop("Time", axis=1, inplace=True)
    csv_data.drop("Class", axis=1, inplace=True)

    i = 0
    while True:
        row = csv_data.sample()
        data = {"vals": row.values.tolist()[0], "id": str(uuid4())}

        m = json.dumps(data)
        producer.produce(TOPIC, m.encode("utf-8"))
        producer.flush()

        i += 1
        time.sleep(random.random())
        if i % 100 == 0:
            print(f"Sent Transaction, id = {i}")


if __name__ == "__main__":
    main()
