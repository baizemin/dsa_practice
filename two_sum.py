def two_sum(nums,target):
    dict = {}
    for i,num in enumerate(nums):
        if target - num in dict:
            return [dict[target - num],i]
        dict[num] = i
    return None

nums_list = [2, 7, 11, 15]
target_value = 9
print(two_sum(nums_list,target_value))


