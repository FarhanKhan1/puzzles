def sol(input_):
    for i in range(int(input_[1])):
        if int(input_[0][-1]) > 0:
            subtracted_value = str(int(input_[0][-1])-1)
            input_[0] = input_[0][:-1] + subtracted_value

        else:
            input_[0] = input_[0][:-1]
        
    return input_[0]

print(sol([i for i in input().split()]))

