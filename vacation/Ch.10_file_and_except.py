from pathlib import Path
import json

"""
path = Path('alice.txt')

def count_words(str_):
    words_dict = {}
    try:
        contents = path.read_text(encoding='utf-8')
        words = contents.lower().split()
        for word in words:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
        if str_ in words_dict:
            print(f"\nThe number of word '{str_}' in {path} is {words_dict[str_]}")
        else:
            none = words_dict.get(str_, 0)
            print(f"\nThe number of word '{str_}' in {path} is {none}")
        return words_dict

    except FileNotFoundError:
        print(f"\nSorry, the file {path} does not exist.")


while True:
    word_ = input("\nPlease enter the word you want to know how many times it appeared in text:")
    print(count_words(word_))
    flag = input("\nIf you want to continue, please enter 'c':")
    if flag == 'c':
        continue
    else:
        break
"""


def get_stored_username(path):
    """저장된 사용자 이름이 있으면 가져옴"""
    if path.exists():
        contents = path.read_text()
        user_info = json.loads(contents)
        return user_info
    else:
        return None
def get_new_username(path, check=None):
    """신규 이름 등록"""
    if check:
        age = input("\nHow old are you?:")
        hobby = input("\nWhat's your hobby?:")
        user_info = {'Name': check, 'Age': age, 'Hobby': hobby}
        contents = json.dumps(user_info)
        path.write_text(contents)
    else:
        name = input("\nWhat's your name?:")
        age = input("\nHow old are you?:")
        hobby = input("\nWhat's your hobby?:")
        user_info = {'Name': name, 'Age': age, 'Hobby': hobby}
        contents = json.dumps(user_info)
        path.write_text(contents)
    return user_info

def greet_user():
    """사용자 이름으로 인사"""
    path = Path('user_info.json')
    name = get_stored_username(path)
    if get_stored_username(path):
        check = input("What's your name?:")
        if check in [value for value in get_stored_username(path).values()]:
            print(f"\nWelcome back, {name['Name']}, you're {name['Age']} years old, and your hobby is {name['Hobby']}!")
        else:
            name = get_new_username(path, check)
            print(f"\nWe'll remember you when you come back, {name['Name']}")
    else:
        name = get_new_username(path)
        print(f"\nWe'll remember you when you come back, {name['Name']}")

greet_user()