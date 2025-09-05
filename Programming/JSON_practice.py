import json
from pathlib import Path

class JSON:
    """test for json module"""
    def __init__(self):
        self.path = Path('C:\\Users\\kimtg\\OneDrive\\Desktop\\python\\Programming\\test.json')

    def input_json(self):
        memo = input("Please type any contents:")
        contents = json.dumps(memo)
        self.path.write_text(contents)

    def output_json(self):
        memo = self.path.read_text().rstrip()
        contents = json.loads(memo)
        print(contents)



