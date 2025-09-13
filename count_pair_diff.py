def count_diff_pair(arr,k):
    arr_set = set(arr)
    count = 0
    for i in arr_set:
        if i+k in arr_set:
            count += 1
    return count

my_nums = [1, 5, 3, 4, 2]
difference = 2
print(count_diff_pair(my_nums,difference))

#this used if we need to include the duplicates

def count_diff_pair2(arr,k):
    freq = {}
    count = 0
    for i in arr:
        if i+k in freq:
            count += freq[i+k]
        if i - k in freq:
            count += freq[i-k]
        freq[i]  =  freq.get(i,0)+1
    return count

arr = [1, 4, 1, 4, 5]
k = 3
print(count_diff_pair2(arr,k))