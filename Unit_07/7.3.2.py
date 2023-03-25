def check_win(secret_word, old_letters_guessed):
    return all([l in old_letters_guessed for l in secret_word])
