HANGMAN_PHOTOS = {
1:r"""
    x-------x""",
2:r"""
    x-------x
    |
    |
    |
    |
    |
    """,

3:r"""
    x-------x
    |       |
    |       0
    |
    |
    |
    """,

4:r"""
    x-------x
    |       |
    |       0
    |       |
    |
    |
    """,

5:r"""
    x-------x
    |       |
    |       0
    |      /|\
    |
    |
    """,

6:r"""
    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |
    """,

7:r"""
    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |
    """
}

def print_hangman(num_of_tries):
    print(HANGMAN_PHOTOS[num_of_tries])
