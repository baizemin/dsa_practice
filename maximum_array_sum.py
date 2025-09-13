def max_product(arr):
    curr_min = curr_max = prod =  arr[0]
    for i in arr[1:]:
        if i < 0:
            curr_max,curr_min = curr_min,curr_max
        curr_min = min(curr_min*i,i)
        curr_max = max(curr_max*i,i)
        prod = max(curr_min,curr_max)
    return prod

print(max_product([2,3,-2,4]))

