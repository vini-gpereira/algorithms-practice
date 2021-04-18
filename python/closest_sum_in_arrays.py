def closestSumInArrays(a, b, target):
    n = len(a)
    m = len(b)
    dp = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            current = [a[i], b[j]]
            up = dp[i - 1][j] if i > 0 else None
            left = dp[i][j - 1] if j > 0 else None
            
            upDistance = getDistanceToTarget(target, up)
            leftDistance = getDistanceToTarget(target, left)
            currentDistance = getDistanceToTarget(target, current)

            minDistance = min(currentDistance, upDistance, leftDistance)

            if minDistance == currentDistance:
                dp[i][j] = current
            elif minDistance == upDistance:
                dp[i][j] = up
            else:
                dp[i][j] = left

    return dp[n - 1][m - 1]

def getDistanceToTarget(target, indexes):
    if indexes is None:
        return float('inf')

    x, y = indexes
    return abs(target - x - y)

if __name__ == "__main__":
    a = [-1, 3, 8, 2, 9, 5]
    b = [4, 1, 2, 10, 5, 20]
    target = 24
    res = closestSumInArrays(a, b, target)
    print(res)
