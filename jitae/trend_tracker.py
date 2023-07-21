#https://seo.tbwakorea.com/blog/naver-seo-api-searching-data/

import pandas as pd
import urllib.request
import json


client_id = "AqGpBbKyqoBW2Czv_OyV"
client_secret = "mdMuLSucIx"

url = "https://openapi.naver.com/v1/datalab/search"
body = "{\
         \"startDate\":\"2023-06-01\",\
         \"endDate\":\"2023-06-02\",\
         \"timeUnit\":\"date\",\
         \"keywordGroups\":[{\"groupName\":\"한글\",\"keywords\":[\"한글\",\"korean\"]},\
                             {\"groupName\":\"영어\",\"keywords\":[\"영어\",\"english\"]}\
                            ],\
         \"device\":\"pc\",\
         \"ages\":[\"1\",\"2\"],\
         \"gender\":\"f\"\
         }";

request = urllib.request.Request(url)
request.add_header("X-Naver-Client-Id",client_id)
request.add_header("X-Naver-Client-Secret",client_secret)
request.add_header("Content-Type","application/json")

response = urllib.request.urlopen(request, data=body.encode("utf-8"))

rescode = response.getcode()

if(rescode==200):
    response_body = response.read()
    response_data = response_body.decode('utf-8')
else:
    print("Error Code:" + rescode)

result = json.loads(response_data)

print(result)

date = [a['period'] for a in result['results'][0]['data']]
ratio_data1 = [a['ratio'] for a in result['results'][0]['data']]
ratio_data2 = [a['ratio'] for a in result['results'][1]['data']]

pd.DataFrame({'date':date,
        'seraching_result':ratio_data1,
        'searching_result2':ratio_data2})