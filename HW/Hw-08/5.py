import pickle


def calculate_divides(file_path: str) -> list[float | None]:
    """Unpickled File & Returned Result Divide Numbers"""

    file = open(file_path, "rb")
    numbers = pickle.load(file)

    try:
        result = list(map(lambda t: t[0] / t[1], numbers))
    #inja bayad ehtemale in ra edahim ke number 2 ma 0 bashad va agar 0 bashad bayad for bezanim roye listemon
    except ZeroDivisionError:
        result = [None for _ in numbers]
    except TypeError:
        result = [None for _ in numbers]
    #bayad dar har soorat in file baste shavad pas behtar ast dar finally bashad ke dar har sorat ejra shavad
    finally:
        file.close()
        return result


var = calculate_divides("numbers.pickle")
print(var)
