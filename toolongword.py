def sol(_list):
    
    for l in range(len(_list)):
        if len(_list[l])>10:
            _list[l] = _list[l][0] + str(len(_list[l])-2) + _list[l][-1]
            print(_list[l])
        else:
            print(_list[l])

    return _list
n = int(input())
list_ = list()
for i in range(n):
    list_.append(input().lower())

sol(list_)        

