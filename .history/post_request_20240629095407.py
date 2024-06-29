import requests
import json

url = "http://localhost:5000//api/deployment"
data = {
    "message": "what are the best pesticides for "
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, data=json.dumps(data), headers=headers)

print(response.json())