def sol(s):
    if len(s) == 1:
        return 'NO'
    for i in s:
        if int(i) != 4:
            if int(i) != 7:
                return 'NO'
            
    return 'YES'


print(sol(input()))

