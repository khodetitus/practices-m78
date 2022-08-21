from abc import abstractmethod, ABC
import pickle
from datetime import datetime
from Subway.models.logger import *
from Subway.exceptions import NotEnoughBalanceError, ExpiredError


class Card(ABC):
    @abstractmethod
    def __init__(self, name: str, validity: int) -> None:
        self.name = name
        self.validity = validity
        logger.info(f"{self.name} with {self.validity}has created!!")
        with open("cards.pickle", "ab") as file:
            pickle.dump(self, file)
            file.write(b"\n")

    def payment(self, value):
        if value <= self.validity:
            self.validity -= value
            print("Transaction Successful!!")
        else:
            logger.error("NotEnoughBalanceError insufficient inventory")
            raise NotEnoughBalanceError("insufficient inventory")


class SingleTableCard(Card):
    def __init__(self, name, validity):
        super().__init__(name, validity)

    @property
    def validity(self):
        return self._validity

    @validity.setter
    def validity(self, value):
        if value < 0:
            logger.error("NotEnoughBalanceError insufficient inventory")
            raise NotEnoughBalanceError("insufficient inventory")
        else:
            self._validity = value

    def __repr__(self):
        return f"My Card Name:{self.name} and Balance is {self.validity}"


class CreditCard(Card):
    def __init__(self, name, validity):
        super().__init__(name, validity)

    @property
    def validity(self):
        return self._validity

    @validity.setter
    def validity(self, value):
        if 0 < value:
            self._validity = value
        else:
            logger.error("NotEnoughBalanceError insufficient inventory")
            raise NotEnoughBalanceError("insufficient inventory")

    def __repr__(self):
        return f"{self.name} and your balance is {self.validity}"


class TermCard(Card):
    def __init__(self, name, validity, end_of_card: datetime):
        super().__init__(name, validity)
        self._end_of_card = end_of_card

    @property
    def validity(self):
        return self._validity

    @validity.setter
    def validity(self, value):
        if 0 < value:
            self._validity = value
        else:
            logger.error("NotEnoughBalanceError insufficient inventory")
            raise NotEnoughBalanceError("insufficient inventory")

    @property
    def end_of_card(self):
        return self._end_of_card

    @end_of_card.setter
    def end_of_card(self, value):
        if self._end_of_card < value(datetime.today()):
            logger.error("ExpiredError Card is Expired")
            raise ExpiredError("Card is Expired")

    def __repr__(self):
        return f"{self.name} and your balance is {self.validity} and expiration date your card is {self.end_of_card}"


# obj1 = SingleTableCard("Single Card", 2)
# obj2 = CreditCard("Credit Card", 50)
# obj3 = TermCard("Term Card", 100, datetime(2022, 9, 20))
# obj1.payment(2)
# obj2.payment(2)
# obj3.payment(2)
# print(obj1.validity)
# print(obj2.validity)
# print(obj3.validity)
