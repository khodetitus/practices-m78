from Subway.models.user import *
from Subway.models.logger import *
from Subway.exceptions import AccessDeniedError


class Admin(User):
    admins_dict = {}

    def __init__(self, username, password, bank_account):
        super().__init__(username, password, bank_account)
        self.id_manager = str(uuid.uuid4().node)
        self.__class__.admins_dict[username, password] = self
        logger.info(f"{self.username} has login!!!")

    @classmethod
    def login(cls, username, password):
        if (username, password) in cls.admins_dict:
            return cls.admins_dict[username, password]
        else:
            logger.info("AccessDeniedError admin access denied")
            raise AccessDeniedError("admin access denied")

# bank2 = BankAccount("blue", 12123, 100)
# user2 = Admin("masoud", "12314", bank2)
# print(Admin.login("masoud", "12314"))
