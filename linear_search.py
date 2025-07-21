def linear_search(arr,key):
    for i in range(len(arr)):
        if arr[i] == key:
            return True
    return False

arr = [1,5,33,4,5,6]
key = 6
print(linear_search(arr,key))