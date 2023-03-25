def numbers_count(my_str):
    return len(list(filter(lambda letter: letter.isdigit(), my_str)))


def letters_count(my_str):
    return len(my_str) - numbers_count(my_str)


def numbers_letters_count(my_str):
    return [numbers_count(my_str), letters_count(my_str)]
