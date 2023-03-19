from termcolor import cprint

ASCII_ART = r"""picture 1:
    x-------x

picture 2:
    x-------x
    |
    |
    |
    |
    |

picture 3:
    x-------x
    |       |
    |       0
    |
    |
    |

picture 4:
    x-------x
    |       |
    |       0
    |       |
    |
    |

picture 5:
    x-------x
    |       |
    |       0
    |      /|\
    |
    |

picture 6:
    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |

picture 7:
    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |"""

cprint(ASCII_ART, "green")