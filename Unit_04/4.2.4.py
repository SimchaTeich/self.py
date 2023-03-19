from calendar import day_name, weekday

date = input("Enter a date: ")
d, m, y = [int(i) for i in date.split("/")]
print(day_name[weekday(y, m, d)])