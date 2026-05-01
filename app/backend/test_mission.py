import requests
import json

url = "http://127.0.0.1:8001/run-mission"
data = {"prospect_name": "Sundar Pichai", "company": "Google"}

try:
    with requests.post(url, json=data, stream=True) as r:
        for line in r.iter_lines():
            if line:
                print(line.decode('utf-8'))
except Exception as e:
    print(f"Error: {e}")
