def first_occurrence(arr,target):
    left,right = 0,len(arr)-1
    res = -1
    while left <= right:
        mid = left + (right-left)//2
        if arr[mid] == target:
            res = mid
            right = mid -1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid -1
    return res

def last_occurrence(arr,target):
    left , right  = 0,len(arr)-1
    res = -1
    while left <= right:
        mid = left+(right-left)//2
        if arr[mid] == target:
            res = mid
            left = mid+1
        elif arr[mid] < target:
            left = mid+1
        else:
            right =  mid-1
    return res

arr = [1,2,2,2,3,4,5]
print("First:", first_occurrence(arr, 2))
print("Last:", last_occurrence(arr, 2))

