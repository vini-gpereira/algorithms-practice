def maxNonContiguousSubArray(arr):    
    if arr is None or len(arr) == 0:
        return None

    including = 0
    excluding = 0

    for i in arr:
        newExcluding = max(including, excluding)
        including = excluding + i
        excluding = newExcluding

    return max(including, excluding)

if __name__ == "__main__":
    arr = [2, 4, 6, 3, 5]
    print(maxNonContiguousSubArray(arr))
