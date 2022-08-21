class NotEnoughBalanceError(Exception):
    pass


class ExpiredError(Exception):
    pass


class CardNotFoundError(Exception):
    pass


class RemainingError(Exception):
    pass


class WithdrawError(Exception):
    pass


class DepositError(Exception):
    pass


class TransferError(Exception):
    pass


class AccessDeniedError(Exception):
    pass


class UsernameWrongError(Exception):
    pass


class PasswordWrongError(Exception):
    pass


class IdNotFoundError(Exception):
    pass
