import requests
import json
URL="http://127.0.0.1:4444/cr/"
# r=requests.get(url=URL)
data={
     'username':'sauarabh',
     'email':'raghavsaurabh337@gmail.com',
     'password':'raghav@123',
}
json_data=json.dumps(data)
r= requests.post(url=URL,data=json_data)
# data=r.json()
print(r)