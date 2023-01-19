def sol(word):
    upper = 0
    lower = 0
    for i in word:
        if i.islower():
            lower+=1
        else:
            upper+=1

    if upper > lower:
        return word.upper()
    else:
        return word.lower()


print(sol(input()))

