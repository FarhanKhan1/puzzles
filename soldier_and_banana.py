def sol(k,n,w):
    cost = 0
    for i in range(1, w+1):
        cost += k*i
    if cost-n < 0:
        return 0
    return cost-n

values = [int(i) for i in input().split()]
print(sol(values[0], values[1], values[2]))

