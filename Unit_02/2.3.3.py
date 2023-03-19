number = int(input("Enter three digits (each digit for one pig): "))

number, digit_3 = divmod(number, 10)
number, digit_2 = divmod(number, 10)
digit_1 = number

s = digit_1 + digit_2 + digit_3
print(s)
print(s // 3)
print(s % 3)
print(s % 3 == 0)