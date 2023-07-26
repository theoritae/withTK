from confluent_kafka import Producer

# Kafka 서버 및 토픽 설정
bootstrap_servers = '192.168.206.131:9092'
topic = 'stream-card'

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
    message = "testmessage testmessage testmessage testmessage testmessage testmessage testmessage testmessage testmessage "
    producer.produce(topic, value=message, callback=delivery_report)

# 메시지 전송 완료 대기
producer.flush()

