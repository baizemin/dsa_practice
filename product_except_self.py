def product_except_self(arr):
    res = [1]*len(arr)
    prefix = 1
    for i in range(len(arr)):
        res[i] = prefix
        prefix *= arr[i]
    suffix = 1
    for i in range(len(arr)-1,-1,-1):
        res[i]*=suffix
        suffix *= arr[i]

    return res

print(product_except_self([1,2,3,4]))

