def find_low_index(arr, key):
    n = len(arr)
    return _find_low_index(arr, key, 0, len(arr), n)

def find_high_index(arr, key):
    return _find_high_index(arr, key, 0, len(arr), 0)

def _find_low_index(arr, key, start, end, low):
    mid = (start + end) // 2

    if start >= end:
        return -1

    if arr[mid] > key:
        return _find_low_index(arr, key, start, mid, low)
    elif arr[mid] < key:
        return _find_low_index(arr, key, mid + 1, end, low)
    
    lessIdx = _find_low_index(arr, key, start, mid, low)

    if lessIdx >= 0:
        return lessIdx

    return mid

def _find_low_index(arr, key, start, end, low):
    mid = (start + end) // 2

    if start >= end:
        return -1

    if arr[mid] > key:
        return _find_low_index(arr, key, start, mid, low)
    elif arr[mid] < key:
        return _find_low_index(arr, key, mid + 1, end, low)
    
    lessIdx = _find_low_index(arr, key, start, mid, low)

    if lessIdx >= 0:
        return lessIdx

    return mid

def _find_high_index(arr, key, start, end, high):
    mid = (start + end) // 2

    if start >= end:
        return -1

    if arr[mid] > key:
        return _find_high_index(arr, key, start, mid, high)
    elif arr[mid] < key:
        return _find_high_index(arr, key, mid + 1, end, high)

    highIdx = _find_high_index(arr, key, mid + 1, end, high)    

    if highIdx >= 0:
        return highIdx

    return mid

def printResult(arr, low, high):
    print("(low, high) =", low, high)

    if low >= 0:
        print("low:", arr[low])
        print("high:", arr[high])
        if low - 1 >= 0:
            print("previous to low:", arr[low - 1])
        else:
            print("No previous to low")

        if high + 1 < len(arr):
            print("next to high:", arr[high + 1])
        else:
            print("No next to high")
    else:
        print("No number found")

if __name__ == "__main__":
    arr = [1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6]
    key = 2
    low, high = find_low_index(arr, key), find_high_index(arr, key)
    printResult(arr, low, high)
