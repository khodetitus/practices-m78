from person import Person
import logging

logger_sub = logging.getLogger("sub-logger")

c_handler = logging.StreamHandler()
f_handler = logging.FileHandler("Sample.log")

c_handler.setLevel(logging.INFO)
f_handler.setLevel(logging.INFO)

c_format = logging.Formatter("%(asctime)s-%(name)-10s-%(levelname)-16s-%(message)s")

c_handler.setFormatter(c_format)
f_handler.setFormatter(c_format)

logger_sub.addHandler(c_handler)
logger_sub.addHandler(f_handler)


def sub(a, b):
    if b != 0:
        logger_sub.debug("a/b=" + str(a / b))
        return a / b
        # logging.debug("a/b=" + str(a / b))#dakhele indent nabayd bad az return chizi benevisim
        # behtar hast ke dakhele massage log ha amliyate mohasebati najam nadahim vali anjam bedim error nemigire
    logger_sub.error("Divide by zero!")


def count_log(file_name, level):
    with open("Person.log", "r") as f:
        result = f.readlines()
        counter = 0
        for i in result:
            if level.upper() in i:
                counter += 1
    return counter


print(sub(2, 3))
print(sub(2, 0))

p1 = Person("ali", "alavi", 23)
p2 = Person("gholi", "gholami", -23)
print(count_log("Person.log", "critical"))
print(count_log("Person.log", "error"))
