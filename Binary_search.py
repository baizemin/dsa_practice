def binary_search(arr,key) :
    l = 0
    h = len(arr)-1
    while l <= h :
        mid = (l+h)//2
        if arr[mid] == key :
            return mid
        elif arr[mid] > key :
            h = mid-1
        elif arr[mid] < key :
            l = mid+1
    return -1
arr = [1,2,3,4,5,6]
key = 6
print(binary_search(arr,key))