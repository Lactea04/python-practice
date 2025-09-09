import json
from json import JSONDecodeError
from pathlib import Path


class Contact:
    def __init__(self, path=''):
        self.path = Path(path)
        self.data =[]
        try:
            contents = self.path.read_text(encoding="utf-8")
            self.data = json.loads(contents)
        except FileNotFoundError:
            pass

    def save_information(self):
        user_info = {}
        name = input("What is your name?"
                     "(ex: David):")
        for data in self.data:
            if name == data['name']:
                return f"\n{name}! your data is already saved before. please use another menu!"
            else:
                pass
        phone_number = input("What is your phone number? "
                             "(ex: XXX-XXXX-XXX):")
        email = input("What is your Email?"
                      "(ex: abc@gmail.com):")
        user_info['name'] = name
        user_info['phone_number'] = phone_number
        user_info['email'] = email
        self.data.append(user_info)
        contents = json.dumps(self.data, ensure_ascii=False, indent=4)
        self.path.write_text(contents, encoding="utf-8")
        return user_info

    def call_information(self, name):
        try:
            contents = self.path.read_text(encoding="utf-8")
            user_data = json.loads(contents)
            for user_info in user_data:
                if user_info['name'] == name:
                    return user_info
                else:
                    pass
        except FileNotFoundError:
            print("File is not exist yet please use the menu number (1)")
            return None
        except JSONDecodeError:
            print("The data is damaged")
            return None

    def show_all_data(self):
        try:
            contents = self.path.read_text(encoding="utf-8")
            user_data = json.loads(contents)
            return user_data
        except FileNotFoundError:
            print("File is not exist yet please use the menu number (1)")
            return None
        except JSONDecodeError:
            print("The data is damaged")
            return None

    def find_number(self, name):
        try:
            contents = self.path.read_text(encoding="utf-8")
            user_data = json.loads(contents)
            for user_info in user_data:
                if user_info['name'] == name:
                    return f"\n{name}'s phone number is {user_info['phone_number']}"
                else:
                    pass
        except FileNotFoundError:
            print("File is not exist yet please use the menu number (1)")
            return None
        except JSONDecodeError:
            print("The data is damaged")
            return None

    def modify_data(self, name, m_option):
        try:
            contents = self.path.read_text(encoding="utf-8")
            user_data = json.loads(contents)
            for user_info in user_data:
                if user_info['name'] == name:
                    if m_option[0] == 'd':
                        num = user_data.index(user_info)
                        del user_data[num]
                        m_contents = json.dumps(user_data, ensure_ascii=False, indent=4)
                        self.path.write_text(m_contents,encoding="utf-8")
                        return f"\n{user_data}\nThe data has successfully deleted!"
                    elif m_option[0] == 'name':
                        user_info['name'] = m_option[1]
                        m_contents = json.dumps(user_data, ensure_ascii=False, indent=4)
                        self.path.write_text(m_contents,encoding="utf-8")
                        return user_info
                    elif m_option[0] == 'phone_number':
                        user_info['phone_number'] = m_option[1]
                        m_contents = json.dumps(user_data, ensure_ascii=False, indent=4)
                        self.path.write_text(m_contents,encoding="utf-8")
                        return user_info
                    elif m_option[0].lower() == 'email':
                        user_info['email'] = m_option[1]
                        m_contents = json.dumps(user_data, ensure_ascii=False, indent=4)
                        self.path.write_text(m_contents,encoding="utf-8")
                        return  user_info
                    elif m_option[0] == 'b':
                        return "back"
                    else:
                        pass
                else:
                    pass
        except FileNotFoundError:
            print("File is not exist yet please use the menu number (1)")
            return None
        except JSONDecodeError:
            print("The data is damaged")
            return None
