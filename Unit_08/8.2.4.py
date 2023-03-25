def is_anagrams(s1, s2):
    return sorted(list(s1)) == sorted(list(s2))


def sort_anagrams(list_of_strings):
    anagrams_lists = []

    while list_of_strings:
        string = list_of_strings[0]
        anagrams_lists.append(list(filter(lambda x: is_anagrams(string, x), list_of_strings)))
        list_of_strings = list(filter(lambda x: not is_anagrams(string, x), list_of_strings))
    
    return anagrams_lists
