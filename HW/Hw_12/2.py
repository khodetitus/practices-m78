import re
import json
filename= "C:/Users/Amir/Desktop/Maktab78_HW/Maktab78_HW/12/2.json"
class User:
    def __init__(self, full_name, phone , email):
        self.full_name = full_name
        self.phone = phone
        self.email= email
    @property
    def phone(self):
        return self._phone
    @phone.setter
    def phone(self, number):
        pattern=re.compile(r'(0|\+98)?9[0-9]{9}')
        result = pattern.finditer(number)
        for  i in result:
            print(i.group())
            self._phone = i.group()
    @property
    def full_name(self):
        return self._full_name
    @full_name.setter
    def full_name(self,name):
        pattern = re.compile(r'^[a-zA-Z-]{4,14}$')
        result = pattern.finditer(name)
        for  i in result:
            print(i.group())
            self._full_name = (i.group())
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self ,mail):
        pattern=re.compile(r'([a-zA-Z0-9-]+)(\@g?mail)(\.com)')
        result = pattern.finditer(mail)
        for  i in result:
            print(i.group())
            self._email = (i.group())
    def json(self):
        with open(filename,"r") as file:
            data = json.load(file)
        data.append({"full_name":self.full_name ,"email :" :self.email , "Phone:" :self.phone} )
        with open(filename, "w") as file:
            json.dump(data, file)
z=User("amirhossein" , '09109911502', "amir0978@mail.com")
z.json()
