def sol(x):
    count = 0
    if x<=5:
        return 1
    else:
        if x%5:
            return int(x/5)+1
        else:
            return int(x/5)


print(sol(int(input())))

