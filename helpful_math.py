def get_seq(str1):
    arr=str1.split('+')
    arr=[int(i) for i in arr]
    for i in range(len(arr)-1,0,-1):
        for k in range(0,i):
            if arr[i]<arr[k]:
                arr[i],arr[k]=arr[k],arr[i]
        arr[i]=str(arr[i])
    arr[0]=str(arr[0])
    return '+'.join(arr)

if __name__ == '__main__':
    
    s = input()
    print(get_seq(s))


