def duplicate_find(arr):
    slow = arr[0]
    fast = arr[0]

    while True:
        slow = arr[slow]
        fast = arr[arr[fast]]
        if slow == fast: break
    slow = arr[0]
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]
    return slow
def duplicate_find_stable(arr):
    duplicates =  []
    seen = set()
    for num in arr:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)
    return duplicates,seen

arr = [1, 3, 4, 2,2]
print(duplicate_find(arr))
print(duplicate_find_stable(arr))