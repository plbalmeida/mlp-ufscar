from confluent_kafka import Consumer, KafkaException
import json

consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'group2',
    'auto.offset.reset': 'earliest'
})

consumer.subscribe(['fraud_transactions'])


def main():
    try:
        while True:
            msg = consumer.poll(1.0)            
            if msg is None:
                continue
            if msg.error():
                raise KafkaException(msg.error())
            else:
                print(json.loads(msg.value().decode('utf-8')))
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()


if __name__ == "__main__":
    main()
