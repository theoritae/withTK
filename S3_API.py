import boto3
import os

# AWS 계정 정보 설정
aws_access_key_id = 'id'
aws_secret_access_key = 'pwd'

# S3 버킷 이름 설정
bucket_name = '버킷이름'

# 업로드할 파일 경로
file_path = '경로'

# 업로드할 파일 이름
file_name = os.path.basename(file_path)

# S3 클라이언트 생성
s3_client = boto3.client('s3',
                         aws_access_key_id=aws_access_key_id,
                         aws_secret_access_key=aws_secret_access_key)

# CSV 파일 업로드
s3_client.upload_file(file_path, bucket_name, file_name)