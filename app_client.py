import requests
import json

url = 'http://127.0.0.1:5000/userLogin'
body = {
    "userName":"Oriol"
}
headers = {
    'content-type': 'application/json'
}

r = requests.post(url, data=json.dumps(body), headers=headers)
print(r.content)