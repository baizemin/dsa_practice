def lps_arry(p):
    m = len(p)
    lps = [0]*m
    length = 0
    i = 1
    while i < m:
        if p[i] == p[length]:
            length += 1
            lps[i] = length
            i+=1
        else:
            if length!=0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i+=1
    return lps

def kmp_search(t,p):
    m = len(p)
    n = len(t)
    result = []
    if m == 0 or n < m : return []
    lps  =lps_arry(p)
    i ,j = 0,0
    while i < n:
        if t[i] == p[j]:
            i+=1
            j+=1
        if j == m :
            result.append(i-j)
            j = lps[j-1]
        elif i < n and t[i] != p[j]:
            if j!=0:
                j = lps[j-1]
            else:
                 i+=1
    return result

print(kmp_search("abcdefg","defg"))






