import requests


#Data_url
url = "https://jonghyup.com/tmp/data.json"

#Get data as JSON form
contents = requests.get(url).json()
#Representative data
#{'items': [{'index': 1, 'age': 35, 'name': 'Allison', 'email': 'alan@branch.st', 'private': {'married': False, 'weight': 35}},...

#Transform dictionary to list, 10 elements in list
contents = contents['items']

def program1():
    """Print the user's information in the format: name, age, email"""
    for info in contents:
        print(f"name: {info['name']}, age: {info['age']}, email: {info['email']}")

def program2():
    """When user's age is 20 and over, print the user's information in the format: name, age, email"""
    for info in contents:
        if info['age'] >= 20:
            print(f"name: {info['name']}, age: {info['age']}, email: {info['email']}")

def program3():
    """When user's weight is 50 and over, print the user information in the format: name, age, weight"""
    for info in contents:
        if info['private']['weight'] >= 50:
            print(f"name: {info['name']}, age: {info['age']}, weight: {info['private']['weight']}")

def flag():
    option = input("_"*100 + "\nIf you want to quit the program, please type the 'q' or 'Q'. Else: continue\n"
                   "Text:")
    if option.lower() == 'q':
        return False
    else:
        return True

#Run program
while True:
    menu = input("\nPlease type the number of program you want to check.\n"
                 "1: Print the user's information in the format: name, age, email\n"
                 "2: When user's age is 20 and over, print the user's information in the format: name, age, email\n"
                 "3: When user's weight is 50 and over, print the user information in the format: name, age, weight\n"
                 "Number:")
    print("_"*100)
    if int(menu) == 1:
        program1()
        if not flag():
            break
    elif int(menu) == 2:
        program2()
        if not flag():
            break
    elif int(menu) == 3:
        program3()
        if not flag():
            break
    else:
        print("The format you typed is incorrect")
        continue

