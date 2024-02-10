import os
from kafka import KafkaProducer, KafkaConsumer

def main():
    num_mappers, num_reducers = os.getenv("MAP_POD_COUNT", 3), os.getenv("REDUCE_POD_COUNT", 2)
    print(f"Master Running with config mappers : {num_mappers} reducers : {num_reducers}")
    
    producer = KafkaProducer(bootstrap_servers=['kafka-core:9092']) # TODO : Read this from env
    # producer.send('my-topic', key=b'foo2', value=b'bar2')
    # producer.flush()

    print("Messages sent")

    consumer = KafkaConsumer('my-topic', bootstrap_servers=['kafka-core:9092'])
    
    for message in consumer:
        print("%s:%d:%d: key=%s value=%s" % (message.topic, message.partition,
                                          message.offset, message.keydecode('utf-8'),
                                          message.value.decode('utf-8')))

if __name__ == "__main__":
    main()