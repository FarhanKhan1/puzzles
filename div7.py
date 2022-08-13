def sol(l):
    for i in range(len(l)):
        if l[i]%7 != 0:
            l[i] -= l[i]%7
        else:
            continue
    
    return l



t = int(input())
list_ = list()
for i in range(t):
    list_.append(int(input()))

out = sol(list_)
for o in out:
    print(o)

