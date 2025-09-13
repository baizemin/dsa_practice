def more_than_half(arr):
    can = -1
    votes = 0
    for i in arr:
        if votes == 0:
            can = i
            votes += 1
        if can == i:
            votes += 1
        else:
            votes -=1
    c = 0
    for i in arr:
        if i == can:
            c += 1
    if c >= len(arr)//2:
        return can
    else:
        return -1
arr = [ 1, 1, 1, 1, 2, 3, 4 ]
print(more_than_half(arr))