def heap_sort(arr):
    for i in range(len(arr), 0, -1):
        heapify(arr, i, 0)
        swap(arr, 0, i - 1)
        

def heapify(arr, n, i):
    largest = i
    l = (i * 2) + 1
    r = (i * 2) + 2

    if l < n and arr[largest] < arr[l]:
        largest = l
    
    if r < n and arr[largest] < arr[r]:
        largest = r
    
    if largest != i:
        swap(arr, largest, i)
        heapify(arr, n, largest)

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

if __name__ == "__main__":
    arr = [10, 7, 11, 2, 5, 8]
    print(arr)
    heap_sort(arr)
    print(arr)