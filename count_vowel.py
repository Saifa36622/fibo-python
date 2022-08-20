def get_count(sentence):
    y = 0
    x = 0
    while x < len(sentence):
        if (sentence[x] == 'a' or sentence[x] == 'u' or sentence[x] == 'o' or sentence[x] == 'e' or sentence[x] == 'i'):
            y = y + 1
        x = x + 1
        return y
        pass