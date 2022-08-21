import uuid
from Subway.models.card import *
from Subway.models.bank import BankAccount
from Subway.models.logger import *
from Subway.exceptions import UsernameWrongError, PasswordWrongError, IdNotFoundError


class User:
    users_dict = {}

    def __init__(self, username: str, password, bank_account: BankAccount):
        self.username = username
        self.password = password
        self.bank_account = bank_account
        self.wallet = {}
        self.__id_number = str(uuid.uuid4().node)
        self.__class__.users_dict[self.__id_number] = self
        logger.info(f"{self.username} with in balance {self.bank_account}!!")
        with open("user.pickle", "ab") as file:
            pickle.dump(self, file)
            file.write(b"\n")

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, value):
        if len(value) > 5:
            self._username = value
        else:
            logger.error("UsernameWrongError username is not more than 5 character")
            raise UsernameWrongError("username is not more than 5 character")

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if len(value) > 4:
            if value.isalnum():
                self._password = value
            else:
                logger.error("PasswordWrongError password is not alphanumeric")
                raise PasswordWrongError("password is not alphanumeric")
        else:
            logger.error("PasswordWrongError password must be more than 4 character")
            raise PasswordWrongError("password must be more than 4 character")

    def __repr__(self):
        return f"my username is:{self.username}"

    def add_card(self, name, cost):
        if name == "Single Card":
            if self.bank_account.remaining > 2:
                self.bank_account.remaining -= 2
                single_card = SingleTableCard(name, 2)
                self.wallet[name] = single_card
        elif name == "Credit Card":
            if self.bank_account.remaining > cost:
                self.bank_account.remaining -= cost
                credit_card = CreditCard(name, cost)
                self.wallet[name] = credit_card
        elif name == "Term Card":
            if self.bank_account.remaining > cost:
                self.bank_account.remaining -= cost
                term_card = TermCard(name, cost, datetime(2022, 9, 20))
                self.wallet[name] = term_card

    @classmethod
    def login(cls, id_code, password):
        if id_code in cls.users_dict:
            if password == cls.users_dict[id_code].password:
                return cls.users_dict[id_code]
            else:
                logger.error("PasswordWrongError password doesnt match!!")
                raise PasswordWrongError("password doesnt match!!")
        else:
            logger.error("IdNotFoundError id_code not found")
            raise IdNotFoundError("id_code not found")

# obj1 = BankAccount("Blue Bank", 10000, 200)
# obj2 = User("khodetitus", "masoud12345", obj1)
# obj2.add_card("Single Card", 10)
# obj2.add_card("Credit Card", 60)
# obj2.add_card("Term Card", 80)
# print(obj2.wallet)
# obj2.wallet["Single Card"].payment(2)
# obj2.wallet["Credit Card"].payment(2)
# obj2.wallet["Term Card"].payment(2)
# print(obj2.wallet)
