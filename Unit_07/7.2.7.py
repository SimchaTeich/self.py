def arrow(my_char, max_length):
    lines_lengths = list(range(1, max_length)) + list(range(max_length,0,-1))
    return "\n".join(my_char * i for i in lines_lengths)
