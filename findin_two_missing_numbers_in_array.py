import math
def missing_numbers(arr):
    min_ = math.inf
    max_ = -math.inf
    for i in arr:
        if i > max_:
            max_ = i
        if i < min_:
            min_ = i
    # print(max_,min_)
    xor1 = 0
    for i in range(min_,max_+1):
        xor1 ^= i
    xor2 = 0
    for i in arr:
        xor2 ^= i
    missing = xor1 ^ xor2
    setbit = missing & - missing
    num1,num2 = 0,0
    for i in range(min_,max_+1):
        if i & setbit:
            num1 ^= i
        else:
            num2 ^= i
    for num in arr:
        if num & setbit:
            num1 ^= num
        else:
            num2 ^= num
    return num1,num2
arr = [1, 2, 4, 6]
print(missing_numbers(arr))





