def power(x, n):
    powers = {}
    return _power(x, n, powers)

def _power(x, n, powers):
    if n == 1:
        return x

    half = _power(x, n // 2, powers)
    result = half * half

    if n % 2 == 1:
        result *= x

    return result
    


if __name__=="__main__":
    print(power(5, 4))