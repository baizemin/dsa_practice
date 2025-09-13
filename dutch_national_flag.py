def rearraging_elements(nums):
    low,mid,high = 0,0,len(nums)-1
    while mid <= high:
        if nums[mid] == 0:
            nums[low],nums[mid] = nums[mid],nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid+=1
        elif nums[mid] == 2:
            nums[high],nums[mid] = nums[mid],nums[high]
            high -= 1
    return nums

arr = [0, 1, 2, 0, 1, 2]
rearraging_elements(arr)
print(arr)

