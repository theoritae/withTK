import boto3
import json
import pandas as pd
import config_loader
result_array = []

df = pd.DataFrame(data=result_array)
result = df.to_json(orient="split")
parsed = json.loads(result)

ACCESS_KEY = config_loader.access_key
SECRET_KEY = config_loader.secret_key

bucket_name = config_loader.bucket_name #bucket_name 이름에 따라 변경
file_name = config_loader.file_name     #search_news.py에서 받아 오는 걸로?

def upload_file_s3(bucket_name, file_name, file):
    s3 = boto3.client('s3',aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    encode_file = json.dumps(file, indent=4, ensure_ascii=False)
    try:
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=encode_file)
        return True
    except: 
        return False

save = upload_file_s3(bucket_name, file_name + '.json', parsed)