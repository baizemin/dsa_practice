def three_sum(nums , target):
    nums.sort()
    n = len(nums)
    res = []
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        j = i+1
        k = n-1
        while j < k:
            s = nums[i] + nums[j] + nums[k]
            if s == target:
                res.append([nums[i], nums[j], nums[k]])
                j +=1
                k-=1
                while j < k and nums[j] == nums[j-1]:
                    j += 1
                while j < k and nums[k] == nums[k-1]:
                    k -= 1
            elif s < target:
                j += 1
            else:
                k -= 1
    return res

nums = [1, 2, -1, -2, 0, 2, -1, -4]
target = 1
print(three_sum(nums, target))

