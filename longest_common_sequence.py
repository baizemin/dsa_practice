def lcs_dp(x,y):
    if x == y:
        return len(x)
    m,n = len(x),len(y)
    dp = [[0 for _ in range(n+1)]for _ in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

x = "ABCBDAB"
Y = "BDCAB"
print(lcs_dp(x,Y))

#using top-down approach

def lcs_topdown(x,y):
     # if x == y :
     #     return len(x)
     m,n = len(x),len(y)
     dp = [[-1 for _ in range(n+1)]for _ in range(m+1)]
     return lcs_aux(x,y,m,n,dp)


def lcs_aux(x,y,i,j,dp):
    if i == 0 or j == 0:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]
    if x[i-1] == y[j-1]:
        dp[i][j] = 1 + lcs_aux(x,y,i-1,j-1,dp)
    else:
        dp[i][j] = max(lcs_aux(x,y,i-1,j,dp),lcs_aux(x,y,i,j-1,dp))
    return dp[i][j]

x = "ABCBDAB"
y = "BDCAB"
print(lcs_topdown(x,y))