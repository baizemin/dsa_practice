import math
def rod_cut_iterative(prices, n):
    r = [-math.inf] * (n + 1)
    r[0] = 0
    for i in range(1, n + 1):
        q = -math.inf
        for j in range(1, i + 1):
            q = max(q, prices[i - 1] + r[i - j])
        r[i] = q
    return r[n]


prices = [1, 5, 8, 9, 10, 17, 17, 20]

rod_length = 4

tot = rod_cut_iterative(prices, rod_length)

print(tot)
