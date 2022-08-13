def sol(_list, a):
    count=0
    kth_finisher_score = _list[a-1]
    for i in _list:
        if i >=kth_finisher_score and i!=0:
            count+=1
    return count

n, k = [int(x) for x in input().split()]

list_ = [int(x) for x in input().split()] 
#print(list_)
print(sol(list_, k))
#print(sol(list_, k))
        

