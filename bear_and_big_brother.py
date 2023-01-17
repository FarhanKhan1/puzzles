def calculate(bear,bob):
    count = 0
    while True:
        if bear > bob:
            return count

        else:
            bear*=3
            bob*=2
            count+=1


ages = [int(i) for i in input().split()]
print(calculate(ages[0], ages[1]))
