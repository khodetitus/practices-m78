import logging

logger_person = logging.getLogger("person-logger")

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler("Person.log")

c_handler.setLevel(logging.DEBUG)
f_handler.setLevel(logging.DEBUG)

c_format = logging.Formatter("%(asctime)s-%(name)-10s-%(levelname)-16s-%(message)s")

c_handler.setFormatter(c_format)
f_handler.setFormatter(c_format)

logger_person.addHandler(c_handler)
logger_person.addHandler(f_handler)


class Person:
    def __init__(self, name, family, age):
        self.name = name
        self.family = family
        self.age = age
        logger_person.info("Person created! {} {}".format(self.name, self.family))

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, a):
        if a > 0:
            self._age = a
        else:
            logger_person.critical("Invalid age!")
        self._age = 0
