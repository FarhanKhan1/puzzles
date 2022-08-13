def sol(_list, n):
    if _list[0] != 1:
        return _list[i]

    for i in range(1, n):
        #print(_list[i]+1, _list[i+1])
        if _list[i]+1 != _list[i+1]:
            print("+ve indexing")
            return _list[i]+1
            
        #elif _list[-(n-i+1)]-1!=_list[-(n-i+1)]:
            #print("-ve indexing")
            #return _list[n-i+1]-1

print(sol([1,2,4,5], 5))
#print(sol([1,2,3,5], 5))        

        

