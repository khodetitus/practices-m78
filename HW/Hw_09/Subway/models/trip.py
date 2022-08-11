from Subway.models.user import *


class Trip:
    def __init__(self, origin: str, destination: str):
        self.origin = origin
        self.destination = destination

    @property
    def origin(self):
        return self._origin

    @origin.setter
    def origin(self, value):
        if value > 0:
            self._origin = value
        else:
            raise ValueError("Insufficient inventory")

    @property
    def destination(self):
        return self._destination

    @destination.setter
    def destination(self, value):
        if value > 0:
            self._destination = value
        else:
            raise ValueError("Insufficient inventory")
