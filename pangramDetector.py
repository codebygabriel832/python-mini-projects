def is_pandram(sentence):
    Each_Letter = []
    for char in sentence:
        char = char.upper()
        if char not in Each_Letter:
            Each_Letter.append(char)
    
    if len(Each_Letter) >= 26:
        return True
    else: 
        return False
    
    
    
print(is_pandram('Pack my box with five dozen liquor jugs'))