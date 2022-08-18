def armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10

    if num == sum:
        yield True
    else:
        yield False


var = armstrong(153)
print(next(var))
