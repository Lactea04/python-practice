import xml.etree.ElementTree as ET
import requests

url = ('https://api.vworld.kr/req/data?service=data&version=2.0&request=GetFeature&key=&format=xml&errorformat=xml&size=10&page=1&data=LT_P_UTISCCTV&geomfilter=POINT(127.0407943%2037.5589599)&attrfilter=locate:like:%EC%84%9C%EC%9A%B8%ED%8A%B9%EB%B3%84%EC%8B%9C%20%EC%84%B1%EB%8F%99%EA%B5%AC%EC%B2%AD&columns=locate,cctvname,ag_geom&geometry=true&attribute=true&crs=EPSG:4326&domain=')
data = requests.get(url).text

root = ET.fromstring(data)


print(root)