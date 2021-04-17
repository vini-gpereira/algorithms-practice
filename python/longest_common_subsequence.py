def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    for row in range(1, n + 1):
        for col in range(1, m + 1):
            if s1[col - 1] == s2[row - 1]:
                dp[row][col] = dp[row - 1][col - 1] + 1
            else:
                up = dp[row - 1][col]
                left = dp[row][col - 1]
                dp[row][col] = max(up, left)
    return dp[n][m]

if __name__ == "__main__":
    s1 = "AAA"
    s2 = "BBB"
    print(lcs(s1, s2))
