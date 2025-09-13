def sub_array_sum(arr,k):
    prefix = 0
    seen = {0:1}
    count = 0
    for num in arr:
        prefix += num
        if prefix-k in seen:
            count += seen[prefix-k]
        seen[prefix] = seen.get(prefix,0)+1
    return count
print(sub_array_sum([1,2,3],3))