user_input = input("Please enter a string: ")
half = len(user_input) // 2

print(user_input[:half].lower() + user_input[half:].upper())