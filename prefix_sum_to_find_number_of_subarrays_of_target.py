from collections import defaultdict
def find_subarray_sum(arr,target):
    n = len(arr)
    prefix_sum = 0
    count = 0
    freq = defaultdict(int)
    freq[0] = 1
    for i in range(len(arr)):
        prefix_sum += arr[i]
        if prefix_sum - target in freq:
            count+=freq[prefix_sum - target]
        freq[prefix_sum] += 1
    return count

print(find_subarray_sum(nums,target))
