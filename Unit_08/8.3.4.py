def inverse_dict(my_dict):
    new_dict = {v:[] for v in my_dict.values()}
    for key, val in my_dict.items():
        new_dict[val].append(key)
        new_dict[val].sort()
    return new_dict
