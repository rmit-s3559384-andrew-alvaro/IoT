import json
import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos")
data = json.loads(response.text)

print(json.dumps(data, indent = 4))
