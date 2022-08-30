import re
import json

filename = "2.json"


class User:
    data = ""

    def __init__(self, full_name, phone, email):
        self.read()
        self.full_name = full_name
        self.phone = phone
        self.email = email
        self.write()

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, number):
        pattern = re.compile(r'(0|\+98)?9[0-9]{9}')
        result = pattern.finditer(number)
        for i in result:
            print(i.group())
            self._phone = i.group()

    @property
    def full_name(self):
        return self._full_name

    @full_name.setter
    def full_name(self, name):
        pattern = re.compile(r'^[a-zA-Z-]{4,14}$')
        result = pattern.finditer(name)
        for i in result:
            print(i.group())
            self._full_name = (i.group())

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, mail):
        pattern = re.compile(r'([a-zA-Z0-9-]+)(\@g?mail)(\.com)')
        result = pattern.finditer(mail)
        for i in result:
            print(i.group())
            self._email = (i.group())

    def read(self):
        with open(filename, "r") as file:
            self.__class__.data = json.load(file)

    def write(self):
        self.__class__.data.append({"full_name": self.full_name, "email :": self.email, "Phone:": self.phone})
        with open(filename, "w") as file:
            json.dump(self.__class__.data, file)


user = User("masoud", '09120572655', "masoudpro2@mail.com")
