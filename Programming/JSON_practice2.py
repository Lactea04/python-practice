#🧠 심화 과제 (선택 사항)

#여러 명의 연락처를 저장할 수 있도록 리스트 구조 사용하기
#이름을 기준으로 특정 연락처 검색하기
#연락처를 삭제하거나 수정하는 기능 추가하기

from contact_class import Contact
from pathlib import Path


path = Path.cwd() / "info.json"
managements = Contact(path)

#manual
while True:
    message = input("\nHello, which menu do you want to use?\n"
                    "(1) Type an user info, (2) Call an user info, (3)Search the phone number,\n"
                    "(4) Modify data, (else) quit this program\n"
                    "Enter the number of menu (ex:1):")
    if message == "1":
        print(managements.save_information())
    elif message == "2":
        name = input("\nWhose data do you want to call?\n"
                     "if you want to see all data, please type 'all':")
        if not name == 'all':
            info = managements.call_information(name)
            if info is None:
                print("\nThe name you typed is not exist in data.")
            else:
                print(f"\nname : {info['name']}\n"
                      f"phone_number : {info['phone_number']}\n"
                      f"Email : {info['email']}")
        else:
            if managements.show_all_data():
                for user_info in managements.show_all_data():
                    print(user_info)
            elif managements.show_all_data() is None:
                print("There is no data.")
    elif message == "3":
        name = input("\nWhose phone number do you want to find:")
        if name is None:
            print("The name you typed is not exist in data.")
        else:
            print(managements.find_number(name))
    elif message == "4":
        m_name = input("\nWhose data do you want to modify?:")
        info = managements.call_information(m_name)
        if info is None:
            print("\nThe name you typed is not exist in data.")
        else:
            print(f"\nname : {info['name']}\n"
              f"phone_number : {info['phone_number']}\n"
              f"Email : {info['email']}")
            print(f"\nWhich data do you want to modify?")
            while True:
                option = input(f"\n(modify: data_type, data_value) ex: name,Kate\n"
                           f"(delete: data_type, '') ex: phone_number,''\n"
                           f"(delete all data: d, name) ex: d,David \n"
                           f"Back to menu is 'b' ex: b.\n"
                           f"please type what you want to do in the correct form: ")
                m_option = option.split(',')
                result = managements.modify_data(m_name, m_option)
                if result == 'back':
                    break
                else:
                    print(result)
    else:
        break



