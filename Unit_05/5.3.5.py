def distance(num1, num2, num3):
    close = first_is_close(num1, num2, num3)
    num2_far = first_is_far(num2, num1, num3)
    num3_far = first_is_far(num3, num1, num2)
    return close and (num2_far or num3_far)

def first_is_close(num1, num2, num3):
    return abs(num1 - num2) == 1 or abs(num1 - num3) == 1

def first_is_far(num1, num2, num3):
    return abs(num1 - num2) >= 2 and abs(num1 - num3) >= 2