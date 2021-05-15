def palidrome(word):
    rev = str(word)[::-1]

    if (word == rev):
        return True
    if (word != rev):
        return False


