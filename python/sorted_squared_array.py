def getSortedSquaredArray(arr):
    n = len(arr)
    l = 0
    r = n - 1
    result = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        if abs(arr[l]) > abs(arr[r]):
            result[i] = arr[l] * arr[l]
            l += 1
        else:
            result[i] = arr[r] * arr[r]
            r -= 1
    return result

if __name__ == "__main__":
    arr = [-7, -3, -2, 0, 1, 4, 5]
    print(getSortedSquaredArray(arr))

