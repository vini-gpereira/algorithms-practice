def findLongestSubarrayBySum(arr, key):
    i = 0
    j = 0
    s = 0
    res = None

    while j < len(arr):
        s += arr[j]

        if s == key and (res is None or res[1] - res[0] < j - i):
            res = [i + 1, j + 1]
        
        if s > key:
            while i < j and s > key:
                s -= arr[i]
                i += 1

        j += 1

    return res


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 0, 0, 0, 6, 7, 8, 9, 10]
    key = 15
    print(findLongestSubarrayBySum(arr, key))
