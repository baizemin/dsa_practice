def duplicates_find(arr):
    duplicates = []
    for num in arr:
        index = abs(num)-1
        if arr[index] < 0:
            duplicates.append(abs(num))
        else:
            arr[index] = -arr[index]
    return duplicates

nums = [4,3,2,7,8,2,3,1]
print(duplicates_find(nums))
# nums.sort()
# print(nums)


