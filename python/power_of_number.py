def power(x, n):
    powers = {}
    return _power(x, n, powers)

def _power(x, n, powers):
    if n == 1:
        return x
    
    if n in powers:
        return powers[n]

    half = _power(x, n // 2, powers)
    result = half * half

    if n % 2 == 1:
        result *= x

    powers[n] = result

    return result
    


if __name__=="__main__":
    print(power(5, 4))