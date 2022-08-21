from Subway.models.user import *
from Subway.models.logger import *
from Subway.exceptions import CardNotFoundError


class Trip:
    list_of_trips = []

    def __init__(self, origin: str, destination: str, user: User, cost, card):
        self.origin = origin
        self.destination = destination
        self.cost = cost
        self.user = user
        self.pay_trips_cost(card)
        logger.info(f"{self.user} of {self.origin} transfer to {self.destination} with {self.cost}")

    def __repr__(self):
        return f"my origin is{self.origin} transfer to {self.destination} with {self.cost}"

    def pay_trips_cost(self, card):
        if card in self.user.wallet:
            self.user.wallet[card].payment(self.cost)
            self.__class__.list_of_trips.append(self)
        else:
            logger.error("CardNotFoundError Card Not Found")
            raise CardNotFoundError("Card Not Found")

# bank1 = BankAccount("blue bank", 100000, 100)
# user1 = User("Masoud", "masoud12345", bank1)
# user1.add_card("Single Card", 2)
# user1.add_card("Credit Card", 100)
# trip1 = Trip("kermanshah", "tehran", user1, 2, "Credit Card")
