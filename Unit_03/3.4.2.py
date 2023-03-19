user_input = input("Please enter a string: ")
first = user_input[0]
print(first + user_input[1:].replace(first, 'e'))