import requests

url = "https://www.gutenberg.org/cache/epub/2701/pg2701-images.html#link2HCH0001"
contents = requests.get(url)

print(contents.status_code)
