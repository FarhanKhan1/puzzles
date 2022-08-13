def sol(m):
    i = 0
    x = 0
    y = 0
    for l in m:
        
        for j in range(len(l)):
            if m[i][j]==1:
                #print(i,'x',j)
                x = i
                y= j
                break
        i+=1 
    
    c = abs(2-x)
    d= abs(2-y)
    print(c+d)


m_ = list()
for i in range(5):
    l_ = list()
    l_ = [int(x) for x in input().split()]
    m_.append(l_)    

sol(m_)

