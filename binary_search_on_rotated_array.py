def binary_search_on_rotated_array(arr,left,right,target):
    while left <= right:
        mid  = left + (right-left)//2
        if arr[mid] == target :
            return mid
        if arr[left] <= arr[mid]:
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid+1
        elif arr[mid] <= arr[right]:
            if arr[mid] <= target < arr[right]:
                left = mid +1
            else:
                right = mid - 1
    return -1

rotated_array = [4, 5, 6, 7, 0, 1, 2]
target1 = 0
print(binary_search_on_rotated_array(rotated_array,0,len(rotated_array)-1,target1))
