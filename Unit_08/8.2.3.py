def mult_tuple(tuple1, tuple2):
    list_by_tuple1_first = [(i, j) for i in tuple1 for j in tuple2]
    list_by_tuple1_second = [(j, i) for i in tuple1 for j in tuple2]
    return list_by_tuple1_first + list_by_tuple1_second
