from faker import Faker
import random
from datetime import datetime, timedelta
import boto3

card_type_list = ["VISA", "MASTER", "JCB", "UnionPay", "Domestic"]
merchant_list = ["식품 및 식료품", "의류 및 패션", "가전제품", "여행 및 숙박", "교통 및 주유", "레저 및 엔터테인먼트", "건강 및 미용", "온라인 쇼핑", "교육 및 교재", "기타"]
start_date_str = "2023-01-01T00:00:00Z"
end_date_str = "2023-12-31T23:59:59Z"
format_str = "%Y-%m-%dT%H:%M:%SZ"

def generate_random_datetime(start_date_str, end_date_str, format_str):

    start_date = datetime.strptime(start_date_str, format_str)
    end_date = datetime.strptime(end_date_str, format_str)
    time_range = (end_date - start_date).total_seconds()
    random_seconds = random.randint(0, int(time_range))
    random_datetime = start_date + timedelta(seconds=random_seconds)
    formatted_datetime = random_datetime.strftime(format_str)

    return formatted_datetime

def generate_batch():

    faker = Faker("ko_KR")

    card_number = str(random.randint(pow(10, 16), pow(10, 17)-1))
    card_type = random.choice(card_type_list)
    card_holder_name = faker.name()
    expiration_date = str(random.randint(00,12))+"/"+str(random.randint(2019,2029))
    cvv = str(random.randint(100, 999))

    adress = faker.address()
    postal_code = faker.postcode()

    amount = str(random.randint(10, 100)*1000)
    merchant = random.choice(merchant_list)
    date = generate_random_datetime(start_date_str, end_date_str, format_str)

    single_batch = "{\"card\":{\"cardNumber\":\""+card_number+"\",\"cardType\":\""+card_type+"\",\"cardHolderName\":\""+card_holder_name+"\",\"expirationDate\":\""+expiration_date+"\",\"cvv\":\""+cvv+"\",\"billingAddress\":{\"adress\":\""+adress+"\",\"postalCode\":\""+postal_code+"\"}},\"transaction\":{\"amount\":\""+amount+"\",\"merchant\":\""+merchant+"\",\"date\":\""+date+"\"}}"

    return single_batch

# for i in range(99):
#    print(generate_batch())

def generate_stream():
    
    faker =Faker("ko_KR")

    card_number = str(random.randint(pow(10, 16), pow(10, 17)-1))
    card_type = random.choice(card_type_list)
    card_holder_name = faker.name()
    expiration_date = str(random.randint(00,12))+"/"+str(random.randint(2019,2029))
    cvv = str(random.randint(100, 999))

    adress = faker.address()
    postal_code = faker.postcode()

    amount = str(random.randint(10, 100)*1000)
    merchant = random.choice(merchant_list)
    date = datetime.now().strftime(format_str)

    single_stream = "{\"card\":{\"cardNumber\":\""+card_number+"\",\"cardType\":\""+card_type+"\",\"cardHolderName\":\""+card_holder_name+"\",\"expirationDate\":\""+expiration_date+"\",\"cvv\":\""+cvv+"\",\"billingAddress\":{\"adress\":\""+adress+"\",\"postalCode\":\""+postal_code+"\"}},\"transaction\":{\"amount\":\""+amount+"\",\"merchant\":\""+merchant+"\",\"date\":\""+date+"\"}}"

    return single_stream

# while True:
#     print(generate_stream())

# S3 버킷 및 파일 정보 설정
bucket_name = 'searchnewsbucket'
file_name = 'your_file_name'
s3_key = 'stream/'+file_name  # S3에 저장될 파일 경로 및 이름
print(s3_key)
# 스트림 데이터 생성 및 전송
stream_data = generate_stream()  # 스트림 데이터 생성하는 함수 호출
s3 = boto3.client('s3',aws_access_key_id='', aws_secret_access_key='')
s3.put_object(Bucket=bucket_name, Key=s3_key, Body=stream_data)
