def divide(first,second):
    if second != 0:
        return first / second
    else:
        return 'Ошибка'


result1 = divide(69, 3)
print(result1)
result2 = divide(3, 0)
print(result2)