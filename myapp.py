import requests
URL = "http://127.0.0.1:8000/stuinfo/"
req = requests.get(url=URL)
data = req.json()
print(data)