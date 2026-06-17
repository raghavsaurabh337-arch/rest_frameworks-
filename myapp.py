import json
import requests
URl="http://127.0.0.1:8000/student/"
def get_data(id=None):
     data={}
     if id is not None:
          data={"id": id}
     json_data=json.dumps(data)
     r=requests.get(url=URl, data=json_data)
     data=r.json()
     print(data)
# get_data() 

def post_data():
     data={
          'name': 'John',
          'city': 'New York',
          'email': 'john@example.com',
          'clas': '10th'
     } 
     json_data=json.dumps(data)    
     r=requests.post(url=URl, data=json_data)
     data=r.json()
     print(data)
# post_data()     
def update_data():
     data={
          'id': 5,
          'name': 'SAURABH SINGH ',
          'city': 'New York',
          'email': 'john@example.com',
          'clas': 'MCA'
     } 
     json_data=json.dumps(data)    
     r=requests.put(url=URl, data=json_data)
     data=r.json()
     print(data)
# update_data() '

def delete_data():
     data={
          'id': 1,
          
     } 
     json_data=json.dumps(data)    
     r=requests.delete(url=URl, data=json_data)
     data=r.json()
     print(data)
delete_data()     
   
     





          