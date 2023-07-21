import boto3
import json
import pandas as pd

result_array = []

df = pd.DataFrame(data=result_array)
result = df.to_json(orient="split")
parsed = json.loads(result)

#ACCESS_KEY, SECRET_KEY 비활성화 해둠! 왜냐면 public에 올라가는 코드라서... 인생 망할까봐...
ACCESS_KEY = ''
SECRET_KEY = ''

bucket = 'searchnewsbucket' #bucket 이름에 따라 변경
file_name = 'file_name_test'    #search_news.py에서 받아 오는 걸로?
def upload_file_s3(bucket, file_name, file):
    s3 = boto3.client('s3',aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)
    encode_file = json.dumps(file, indent=4, ensure_ascii=False)
    try:
        s3.put_object(Bucket=bucket, Key=file_name, Body=encode_file)
        return True
    except: 
        return False

save = upload_file_s3(bucket, file_name + '.json', parsed)