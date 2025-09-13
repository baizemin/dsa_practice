def finding_k(arr):
    left ,right = 0,len(arr)-1
    if arr[left] < arr[right]:
        return 0
    while left <= right:
        mid = left + (right-left)//2
        if arr[mid-1] > arr[mid]:
            return mid
        if arr[mid] > arr[mid+1]:
            return mid+1
        if arr[left] <= arr[mid]:
            left = mid+1
        else:
            right = mid-1

my_arr = [4, 5, 6, 7, 0, 1, 2]
print(finding_k(my_arr))



