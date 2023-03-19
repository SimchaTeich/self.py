deg = input("Insert the temprature you would like to convert: ").upper()
deg_n = float(deg[:-1])

if deg[-1] == 'C':
    print(str((9 * deg_n + 32 * 5) / 5) + "F") 
else:
    print(str((5 * deg_n - 160) / 9) + "C")