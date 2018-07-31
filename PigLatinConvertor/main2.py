# PygLatin Converter Code
pyg = 'ay'
pyg2 = 'way'


def convertor(str):
    original = str
    
    if len(original) > 0 and original.isalpha():
        word = original.lower()
        first = word[0]
        if first == ('a' or 'e' or 'i' or 'o' or 'u'):
            new_word = word + pyg2
            return new_word
        else:
            new_word = word[1:] + first + pyg
            return new_word
    
    return 'empty'