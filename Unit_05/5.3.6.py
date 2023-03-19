def fix_age(age):
    return 0 if 13 <= age <= 14 or 17 <= age <= 19 else age

def filter_teens(a = 13, b = 13, c = 13):
    return fix_age(a) + fix_age(b) + fix_age(c)