def sol(_string):
    if len(set(_string)) % 2 == 0:
        return "CHAT WITH HER!"
    else:
        return "IGNORE HIM!"

if __name__ == '__main__':                                                                                                                                      
    print(sol(input()))
