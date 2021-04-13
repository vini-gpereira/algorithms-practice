from math import floor

def squareRoot(number):
    if number == 0:
        return 0

    result = _squareRoot(0, number, number)

    if result == -1:
        return None
    
    return result

def _squareRoot(mn, mx, key):
    if mn > mx:
        return -1

    half = (mn + mx) // 2
    halfSquare = half ** 2

    if halfSquare > key:
        return _squareRoot(mn, half - 1, key)
    elif halfSquare < key:
        return _squareRoot(half + 1, mx, key)

    return half

if __name__ == "__main__":
    for i in range(0, 11):
        print(f"{i}: {squareRoot(i)}")
