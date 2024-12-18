import requests

text = "Hello, how are you?"

response = requests.post(
    "http://127.0.0.1:8000/translate/",
    json={"text": text},
    headers={"accept": "application/json"},
)

assert response.status_code == 200
