class Human:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Value is less than zero!")


class SoccerPlayer(Human):
    def __init__(self, salary, position, performance, name, age):
        super().__init__(name, age)
        self.performance = performance
        self.position = position
        self.salary = salary

    @property
    def performance(self):
        return self._performance

    @performance.setter
    def performance(self, value):
        if 0 <= value <= 100:
            self._performance = value
        else:
            raise ValueError("Performance is out of range!!")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if 15 <= value <= 30:
            self._age = value
        else:
            raise ValueError("Player age is out of range!!")

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, value):
        if value >= 0:
            self._salary = value
        else:
            raise ValueError("Salary not be zero!!")


class Coach(Human):
    def __init__(self, salary, start_of_contract, end_of_contract, name, age):
        super().__init__(name, age)
        self.salary = salary
        self.start_of_contract = start_of_contract
        self.end_of_contract = end_of_contract

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if 30 <= value <= 65:
            self._age = value
        else:
            raise ValueError("Coach age is out of range!!")
