def rotateImage(a):
    if a is None:
        return
    
    n = len(a)
    
    if n == 0:
        return
    
    for row in range((n // 2) + 1):
        for col in range(row, n - row - 1):
            rotateMatrixElements(a, n, row, col)

def rotateMatrixElements(m, n, i, j):
    r = i
    c = j
    aux = m[r][c]
    for _ in range(4):
        nr, nc = getRotatedPair(n, r, c)
        m[nr][nc], aux = aux, m[nr][nc]
        r, c = nr, nc

def getRotatedPair(n, row, col):
    center = getCenter(n)
    cartesianRow = row - center
    cartesianCol = col - center
    newCartesianRow = cartesianCol
    newCartesianCol = -cartesianRow
    newRow = newCartesianRow + center
    newCol = newCartesianCol + center
    return int(newRow), int(newCol)

def getCenter(n):
    if n % 2 == 0:
        left = n / 2
        right = left - 1
        return (left + right) / 2
    
    return n // 2

def printMatrix(m):
    n = len(m)
    for row in range(n):
        for col in range(n):
            print(m[row][col], end="\t")
        print()

def createMatrix(n):
    a = [[0 for _ in range(n)] for _ in range(n)]
    counter = 1
    for i in range(n):
        for j in range(n):
            a[i][j] = counter
            counter += 1
    return a

if __name__ == "__main__":
    n = 4
    a = createMatrix(n)
    printMatrix(a)
    rotateImage(a)
    print("----------")
    printMatrix(a)