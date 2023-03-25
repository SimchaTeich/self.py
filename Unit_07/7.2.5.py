def sequence_del(my_str):
    my_str_after_del = my_str[0] if len(my_str) else ''
    
    for letter in my_str:
        if letter != my_str_after_del[-1]:
            my_str_after_del += letter
    
    return my_str_after_del
