def is_valid_input(letter_guessed):
    return len(letter_guessed) == 1 and letter_guessed.isalpha()

def check_valid_input(letter_guessed, old_letters_guessed):
    letter_guessed = letter_guessed.lower()
    return is_valid_input(letter_guessed) and letter_guessed not in old_letters_guessed
