word = input("Enter a word: ")
word = word.replace(" ", "").lower()
print("OK" if word == word[::-1] else "NOT")