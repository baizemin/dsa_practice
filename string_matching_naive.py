def string_matching_naive(s,p):
    n = len(s)
    m = len(p)
    for i in range(n-m):
        is_match = True
        for j in range(m):
            if s[i+j] != p[j]:
                is_match = False
                break
        if is_match:
            return i
    return -1

s = "logarithm"
p = "gar"
print(string_matching_naive(s,p))