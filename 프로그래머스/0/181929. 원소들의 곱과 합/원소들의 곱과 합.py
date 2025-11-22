def solution(num_list):
    flag1 = 1
    flag2 = 0
    for i in num_list:
        flag1 *= i
        flag2 += i
    
    return 1 if flag1 < flag2 ** 2 else 0