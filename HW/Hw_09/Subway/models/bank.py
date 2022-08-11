from Subway.models.logger import *
from Subway.exceptions import RemainingError, WithdrawError, DepositError, TransferError


class BankAccount:

    def __init__(self, name: str, remaining: int, minimum: int = 100):
        self.name = name
        self.remaining = remaining
        self.minimum = minimum
        logger.info(f"{self.name} with {self.remaining} insufficient and minimum of balance is{self.minimum}")

    @property
    def remaining(self):
        return self._remaining

    @remaining.setter
    def remaining(self, value):
        if value >= 100:
            self._remaining = value
        else:
            logger.error("RemainingError remaining must be more than minimum")
            raise RemainingError("remaining must be more than minimum")

    def __repr__(self):
        return f"my balance is {self.remaining}"

    def withdraw(self, cost):
        if self.remaining - cost > self.minimum:
            self.remaining -= cost
            print("Withdrawal was successful!")
        else:
            logger.error("WithdrawErrorWithdraw error")
            raise WithdrawError("Withdraw error")

    def deposit(self, cost):
        if cost > 0:
            self.remaining += cost
            print("Deposit was successful!")
        else:
            logger.error("DepositError deposit error")
            raise DepositError("deposit error")

    def transfer(self, other, cost):
        if self.remaining - cost > self.minimum:
            self.remaining -= cost
            other.remaining += cost
            print("Transfer was successful!")
        else:
            logger.error("TransferError transfer error")
            raise TransferError("transfer error")

# obj1 = BankAccount("Blue Bank", 10000)
# print(obj1)
