import re
import requests


url = "https://jonghyup.com/tmp/sampledata.txt"
contents = requests.get(url).text

#phone number
phone_numbers = re.findall(r"010-\d{4}-\d{4}", contents) #list
print(f"The number of Phone number: {len(phone_numbers)}")

#resident registration number
resident_registration_numbers = re.findall(r"\d{6}-[1-4]\d{6}", contents) #list
print(f"The number of resident registration number: {len(resident_registration_numbers)}")

#class number
class_numbers = re.findall(r"20\d{7}", contents) #list
print(f"The number of class number: {len(class_numbers)}")

#corded telephone number
corded_telephone_numbers = re.findall(r"0[02-9]\d?-[1-9]\d{2}\d?-\d{4}", contents) #list
print(f"The number of Corded_telephone_number: {len(corded_telephone_numbers)}")

#email
emails = re.findall(r"\w+@[\w\.]+", contents) #list
print(f"The number of email: {len(emails)}")

#date
dates = re.findall(r"20\d{2}-\d{2}-\d{2}", contents) #list
print(f"The number of date: {len(dates)}")