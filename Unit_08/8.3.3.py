def count_chars(my_str):
    my_str = my_str.replace(' ', '')
    return {letter:my_str.count(letter) for letter in my_str}
