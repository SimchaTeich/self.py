def find_missing_from_list(numbers_list):
    """
    Find the missing value from list.
    :param number_list: list of integer from 1 to n,
                        without one number.
    :type number_list: list of integers
    :return: the missing value
    :rtype: int
    """
    sum_without_missing = sum(range(len(numbers_list) + 1 + 1))
    sum_with_missing = sum(numbers_list)
    
    return sum_without_missing - sum_with_missing


def who_is_missing(file_name):
    # open file
    file_object = open(file_name, 'r')

    # get file content and close the file.
    list_of_numbers = [int(n) for n in file_object.read().split(',')]
    file_object.close()

    # get the missing number
    missing_num = find_missing_from_list(list_of_numbers)  

    # wrtie the answer to new file
    output_file = open("found.txt", 'w')
    output_file.write(str(missing_num))
    output_file.close()

    # return the missing value
    return missing_num
