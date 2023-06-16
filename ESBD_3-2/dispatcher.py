from confluent_kafka import Consumer, KafkaException
import zmq
import json

# set up ZeroMQ context and socket
context = zmq.Context()
socket = context.socket(zmq.PUSH)
socket.bind("tcp://*:5557")

# set up Kafka consumer
consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'group1',
    'auto.offset.reset': 'earliest'
})

TOPIC = 'creditcard_transactions'
consumer.subscribe([TOPIC])


def main():
    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())
            else:
                transaction = json.loads(msg.value().decode('utf-8'))
                print(f'{transaction}')
                print('')
                socket.send_json(transaction)
    except KeyboardInterrupt:
        pass

    finally:
        consumer.close()


if __name__ == "__main__":
    main()
