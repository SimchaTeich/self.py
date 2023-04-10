HANGMAN_ASCII_ART = """  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""

MAX_TRIES = 6

HANGMAN_PHOTOS =\
{
    0:r"""
        x-------x""",
    1:r"""
        x-------x
        |
        |
        |
        |
        |
        """,

    2:r"""
        x-------x
        |       |
        |       0
        |
        |
        |
        """,

    3:r"""
        x-------x
        |       |
        |       0
        |       |
        |
        |
        """,

    4:r"""
        x-------x
        |       |
        |       0
        |      /|\
        |
        |
        """,

    5:r"""
        x-------x
        |       |
        |       0
        |      /|\
        |      /
        |
        """,

    6:r"""
        x-------x
        |       |
        |       0
        |      /|\
        |      / \
        |
        """
}


def check_win(secret_word, old_letters_guessed):
    """
    check if all secret letters was guessed
    :param secret_word: the secret word of the game
    :type secret_word: str
    :param old_letters_guessed: words user was guessed
    :type old_letters_guessed: list of strings
    :return: True if old_letters_guessed contains all secret_word letter
    :rtype: bool
    """
    return all([l in old_letters_guessed for l in secret_word])


def show_hidden_word(secret_word, old_letters_guessed):
    """
    Make string that shows just the letter was guessed
    from the secret word.
    For example:
        secret_word = "helloworld"
        old_letters_guessed = ['o', 'l', 'h']
        so function return the string: "h _ l l o _ o _ l _"
    :param secret_word: the secret word of the game
    :type secret_word: str
    :param old_letters_guessed: words user was guessed
    :type old_letters_guessed: list of strings
    :return: string as exaplain abouv
    :rtype: str
    """
    return ' '.join(l if l in old_letters_guessed else '_' for l in secret_word)


def check_valid_input(letter_guessed, old_letters_guessed):
    """
    checks if letter from user is valid guess.
    :param letter_guessed: input from user
    :type secret_word: str
    :param old_letters_guessed: words user was guessed
    :type old_letters_guessed: list of strings
    :return: True if letter_guessed is letter
             that was not guessed before.
    :rtype: bool
    """
    letter_guessed = letter_guessed.lower()
    
    return len(letter_guessed) == 1 and \
            letter_guessed.isalpha() and \
            letter_guessed not in old_letters_guessed


def try_update_letter_guessed(letter_guessed, old_letters_guessed):
    """
    append new letter to old_letters_guessed if can.
    :param letter_guessed: input from user
    :type secret_word: str
    :param old_letters_guessed: words user was guessed
    :type old_letters_guessed: list of strings
    :return: True if letter_guessed was inserted to list of olds.
    :rtype: bool
    """
    if check_valid_input(letter_guessed, old_letters_guessed):
        old_letters_guessed.append(letter_guessed)
        return True
    else:
        print('X')
        print(" -> ".join(sorted(old_letters_guessed)))
        return False


def choose_word(file_path, index):
    """
    take one word from file of words
    :param file_path: path to file woth words.
    :type file_path: str
    :param index: index stars from 1 and can be modulu
    :type index: int
    :return: choosen word from the file
    :rtype: str
    """
    with open(file_path) as f:
        words = f.read().split()
    
    return words[(index-1) % len(words)]


def print_hangman(num_of_tries):
    """
    prints the correct draw of the hangman
    by indexing of the HANGMAN dictionary
    """
    print(HANGMAN_PHOTOS[num_of_tries])


def print_open_screen():
    print(HANGMAN_ASCII_ART + '\n' + str(MAX_TRIES))


def get_secret_word():
    file_path = input("Enter file path: ")
    index = int(input("Enter index: "))
    
    return choose_word(file_path, index)


def main():
    print_open_screen()
    
    # init the game
    old_letters_guessed = []
    secret_word = get_secret_word()
    num_of_tries = 0
    
    # start game
    print("Let’s start!")
    print_hangman(num_of_tries)
    num_of_tries += 1
    print(show_hidden_word(secret_word, old_letters_guessed))
    
    # play while user does not lost the game or he wins
    while num_of_tries <= MAX_TRIES and not check_win(secret_word, old_letters_guessed):
        
        # get some guess
        letter_guessed = input("Guess a letter: ").lower()
        
        # check for valid of the guess
        if try_update_letter_guessed(letter_guessed, old_letters_guessed):
            
            # print the hangman if guess is valid but uncorrect
            if letter_guessed not in secret_word:
               print(":(")
               print_hangman(num_of_tries)
               num_of_tries += 1
            
            print(show_hidden_word(secret_word, old_letters_guessed))
    
    # final msg about win of the game
    print("WIN" if num_of_tries <= MAX_TRIES else "LOSE")


if __name__ == "__main__":
    main()
