def choose_word(file_path, index):
    with open(file_path) as f:
        words = f.read().split()
    
    index -= 1
    index %= len(words)
    
    return len(set(words)), words[index]
