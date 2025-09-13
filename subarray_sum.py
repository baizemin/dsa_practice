def subarray(arr,target):
    curr = 0
    n = len(arr)
    start = 0
    end = 0
    for end in range(len(arr)):
        curr += arr[end]
        while curr > target and start <= end:
            curr -= arr[start]
            start+=1
        if curr == target:
            return [start,end]
    return -1

arr = [1, 4, 20, 3, 10, 5]
target = 33
print(subarray(arr,target))