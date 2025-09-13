from collections import defaultdict
def prefix_sum_subarray(arr,target):
    prefix_sum = 0
    freq = defaultdict(int)
    freq[0] = 1
    count = 0
    for i in arr:
        prefix_sum += i
        if prefix_sum-target in freq:
            count+=freq[prefix_sum-target]
        freq[prefix_sum] += 1
    return count


nums = [1,2,3,0,3]
target = 3
print(prefix_sum_subarray(nums,target))


