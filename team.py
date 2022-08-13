def sol(_list):
    count = 0
    for l_ in _list:
        if (int(l_[0]) + int(l_[1]) + int(l_[2])) >=2:
            count +=1


    return count    

n = int(input())
list_ = list()
for i in range(n):
    l = list()
    l = [x for x in input().split()]
    list_.append(l)

print(sol(list_))

