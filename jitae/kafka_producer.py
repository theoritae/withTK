from confluent_kafka import Producer
from stream_card_generator import generate_stream
import config_loader

# Kafka 서버 및 토픽 설정
bootstrap_servers = config_loader.bootstrap_servers
topic = config_loader.topic

# Kafka 프로듀서 구성
conf = {'bootstrap.servers': bootstrap_servers}

# Kafka 프로듀서 생성
producer = Producer(conf)

# 메시지 전송 콜백 함수
def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed: {err}')
    else:
        print(f'Message delivered to {msg.topic()} [{msg.partition()}]')

# 메시지 생성 및 전송
for i in range(10):
    message = generate_stream()
    producer.produce(topic, value=message, callback=delivery_report)

# 메시지 전송 완료 대기
producer.flush()

