import requests
import json

url = "http://localhost:5000/api/user"
data = {
    "username": "test_user"
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.json())