def longest_consequence(arr):
    arr_set = set(arr)
    longest = 0
    for num in arr_set:
        if num-1 not in arr_set:
            curr = num
            curr_steak = 1
            while curr+1 in arr_set:
                curr += 1
                curr_steak += 1
            longest = max(longest, curr_steak)
    return longest
arr = [100,4,200,2,3,1]
print(longest_consequence(arr))