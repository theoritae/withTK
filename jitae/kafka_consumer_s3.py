from confluent_kafka import Consumer, KafkaException, KafkaError
import s3_uploader


# Kafka 서버 및 토픽 설정
bootstrap_servers = '192.168.206.131:9092'
topic = 'stream-card'
group_id = 's3_upload_group'

# Kafka 컨슈머 구성
conf = {
    'bootstrap.servers': bootstrap_servers,
    'group.id': group_id,
    'auto.offset.reset': 'earliest'
}

# Kafka 컨슈머 생성
consumer = Consumer(conf)

# 토픽 구독
consumer.subscribe([topic])

# 메시지 소비
try:
    while True:
        msg = consumer.poll(1.0)  # 메시지를 폴링하여 가져옵니다. (타임아웃 1.0초)
        if msg is None:
            continue
        if msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                # 토픽의 끝에 도달한 경우
                print(f'Reached the end of the topic: {msg.topic()} [{msg.partition()}]')
            else:
                # 에러가 발생한 경우
                print(f'Error occurred: {msg.error().str()}')
            continue

        # 메시지 처리
        # print(f'Received message: {msg.value().decode("utf-8")}')
        # s3 업로더에 값 담아서 보내기~

except KeyboardInterrupt:
    # 사용자가 중지하면 종료합니다.
    pass

finally:
    # 컨슈머 종료
    consumer.close()