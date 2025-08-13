import math
def rod_cut(prices,n):
    if n == 0:
        return 0
    q = -math.inf
    for i in range(n):
        q = max(q,prices[i]+rod_cut(prices,n-(i+1)))
    return q

prices = [1, 5, 8, 9, 10, 17, 17, 20]
rod_length = 4
tot = rod_cut(prices, rod_length)
print(tot)

