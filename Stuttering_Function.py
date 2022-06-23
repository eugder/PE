def stutter(word):
    st = (word[:2] + "... ")*2
    return (st + word + "?")

print(stutter("in"))