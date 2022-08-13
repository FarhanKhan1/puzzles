def sol(w):
    if w>3:
        if w%2==0:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'

w = int(input())
print(sol(w))


