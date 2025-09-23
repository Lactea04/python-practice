import requests


class DataProcess:
    def __init__(self):
        self.url = "https://jonghyup.com/tmp/data.json"
        self.contents = requests.get(self.url).json()["items"]



    def show_data(self):
        print(self.contents)

    def search_data(self):
        name = input("Please type the name you want to search:")
        for x in self.contents:
            if name in x['name']:
                print(x)


