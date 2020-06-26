number = int(input('Введите число: '))
i = 1
a = 1
number1 = 0
while number1 < 10 and a <=9:
    number1 = number // i % 10 + a
    i *= 10
    while i > number*10:
        a += 1
        i = 1
print(number1 - a)

