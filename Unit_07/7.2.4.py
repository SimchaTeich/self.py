def is_legal(num):
    return '7' not in str(num) and num % 7 != 0


def num_or_BOOM(num):
    return num if is_legal(num) else 'BOOM'


def seven_boom(end_number):
    return [num_or_BOOM(num) for num in range(end_number+1)]
