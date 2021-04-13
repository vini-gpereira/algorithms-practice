def binary_search_rotated(arr, key):
    n = len(arr)
    lowestIdx = find_lowest_number_idx(arr, 0, n, None)
    return _binary_search_rotated(arr, n, key, lowestIdx, lowestIdx + n)

def find_lowest_number_idx(arr, start, end, lowestIdx):
    mid = (start + end) // 2

    if start < end:
        if lowestIdx is None or arr[lowestIdx] > arr[mid]:
            return find_lowest_number_idx(arr, start, mid, mid)
        else:
            return find_lowest_number_idx(arr, mid + 1, end, lowestIdx)

    return lowestIdx

def _binary_search_rotated(arr, n, key, start, end):
    if start >= end:
        return -1

    mid = (start + end) // 2
    midMod = mid % n
    
    if arr[midMod] > key:
        return _binary_search_rotated(arr, n, key, start, mid)
    elif arr[midMod] < key:
        return _binary_search_rotated(arr, n, key, mid + 1, end)

    return midMod


if __name__ == "__main__":
    arr = [180, 200, 220, 0, 20, 30, 40]
    number = 10
    print(binary_search_rotated(arr, number))