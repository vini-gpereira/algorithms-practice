def search(A, B):
        n = len(A)
        return _search(A, B, 0, n - 1)

def _search(A, B, l, r):
    if l > r:
        return -1

    m = (l + r) // 2

    if A[m] == B:
        return m

    if A[m] > A[l]:
        if A[l] <= B < A[m]:
            return _search(A, B, l, m - 1)
        else:
            return _search(A, B, m + 1, r)

    if A[m] < B <= A[r]:
        return _search(A, B, m + 1, r)

    return _search(A, B, l, m - 1)


if __name__ == "__main__":
    arr = [180, 200, 220, 0, 20, 30, 40]
    number = 200
    print(search(arr, number))