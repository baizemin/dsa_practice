def most_repeated(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num, 0) + 1
    max_count = 0
    for count in freq.values():
        if count > max_count:
            max_count = count
    return [(num,count) for num,count in freq.items() if count == max_count]

arr = [0, 1, 2, 0, 1, 2]
print(most_repeated(arr))


