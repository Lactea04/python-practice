import json
import requests


url = "http://swopenapi.seoul.go.kr/api/subway/sample/json/realtimeStationArrival/0/5/%EA%B0%80%EC%B2%9C%EB%8C%80"
contents = requests.get(url).text
data = json.loads(contents)

for x in data:
    print(x)