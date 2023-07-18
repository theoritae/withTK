import csv
from datetime import datetime, timedelta
import random

# CSV 파일 경로
csv_file = r'C:\Users\hank9\Desktop\python\generated_weather_data.csv'

# 시작 날짜와 시간
start_date = datetime(2023, 1, 1)
start_time = datetime(2023, 1, 1, 0, 0)

while True:
    # 데이터 생성
    current_date = datetime.now()
    current_time = datetime.now()

    # 데이터 생성
    date = current_date.strftime('%Y-%m-%d')
    time = current_time.strftime('%H:%M')
    location = random.choice(['서울', '부산', '인천', '대구', '대전', '광주', '수원', '울산', '창원', '세종', '청주', '안양', '고양', '용인', '성남', '부천', '화성', '남양주', '포항', '전주'])
    temperature = round(random.uniform(-10, 40), 1)
    humidity = random.randint(0, 100)
    wind_speed = round(random.uniform(0, 10), 1)
    precipitation = round(random.uniform(0, 30), 1)

    # 데이터 추가
    with open(csv_file, 'a', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, time, location, temperature, humidity, wind_speed, precipitation])

print(f'데이터 생성을 종료합니다. 생성된 데이터는 {csv_file}에 저장되었습니다.')