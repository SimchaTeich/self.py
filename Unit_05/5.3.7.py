def chocolate_maker(small, big, x):
    if (x // 5) > big:
        x -= big * (x // 5)
    else:
        x -= 5 * (x // 5)
    return x - small <= 0