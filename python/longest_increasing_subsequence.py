def lis(A):
    N = len(A)
    dp = [0 for _ in range(N)]

    for i in range(N):
        less = [dp[j] if A[i] > A[j] else 0 for j in range(i)]
        dp[i] = max(less, default = 0) + 1

    return dp[N - 1]

if __name__ == "__main__":
    A = [3, 1, 8, 2, 5]
    print(lis(A))
