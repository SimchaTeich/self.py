def sort(file_object):
    """
    Prints all word in the file,
    in sorted alphabeticly list.
    :param file_object: file object
    :type file_object: _io.TextIOWrapper (just text file)
    """
    print(sorted(set(file_object.read().split())))


def rev(file_object):
    """
    Print in reverse order
    all the letters for each line
    :param file_object: file object
    :type file_object: _io.TextIOWrapper (just text file)
    """
    lines = file_object.readlines()
    for line in lines: print(line[::-1])


def last(file_object):
    """
    Ask for number n, and print the
    last n lines in the file.
    :param file_object: file object
    :type file_object: _io.TextIOWrapper (just text file)
    """
    n = int(input("Enter a number: "))
    lines = file_object.readlines()[-n:]
    for line in lines: print(line)


TASKS =\
{
    'sort' : sort,
    'rev' : rev,
    'last' : last
}


def main():
    file_path = input("Enter a file path: ")
    task = input("Enter a task: ")

    file_object = open(file_path, 'r')

    # call the right task.
    TASKS[task](file_object)
    
    file_object.close()


if __name__ == '__main__':
    main()
