import requests
import json

url = "http://localhost:5000//api/deployment"
data = {
    "message": "what are the best pesticides for crops in Kerala?",
    "context_length":2048
}

headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, data=json.dumps(data), headers=headers)

output  =  response.json()
result = output["response"]
print("final response: " ,result)