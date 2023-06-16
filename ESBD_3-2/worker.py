import zmq
import joblib
import pandas as pd
from confluent_kafka import Producer
import json

context = zmq.Context()
socket = context.socket(zmq.PULL)
socket.connect("tcp://localhost:5557")

TOPIC = "fraud_transactions"
producer = Producer({'bootstrap.servers': 'localhost:9092'})


def main():
    loaded_svc = joblib.load("svm.joblib")
    while True:
        transaction = socket.recv_json()
        input_arr = pd.array(transaction["vals"]).reshape(1, -1)
        result = loaded_svc.predict(input_arr)[0]
        if result == 1:
            print(f'{result}')
            print('')
            producer.produce(TOPIC, json.dumps({
                'fraud': True,
                'transactionId': transaction['id']
            }))
            producer.flush()


if __name__ == "__main__":
    main()
