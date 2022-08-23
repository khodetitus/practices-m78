import sys

numbers = sys.argv[1::]
print(numbers)
count = 0
if numbers:
    for i in numbers:
        count += int(i)
    else:
        raise SyntaxError("You must enter integer")
grade = count / len(numbers)
print(grade)
