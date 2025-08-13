import math
def rod_cut(prices, n):
    if n == 0:
        return 0
    r = [-math.inf]*(n+1)
    return rod_cut_aux(prices,n,r)
def rod_cut_aux(prices, n, r):
    q =  0
    if r[n] >= 0 :
        return r[n]
    if n == 0:
        q = 0
    for i in range(1,n+1):
        q = max(q,prices[i-1]+rod_cut_aux(prices, n-i,r))
    r[n] = q
    return q


prices = [1, 5, 8, 9, 10, 17, 17, 20]

# Length of the rod to be cut.
rod_length = 4

tot = rod_cut(prices, rod_length)

print(tot)


