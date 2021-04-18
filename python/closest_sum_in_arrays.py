def closestSumInArrays(a, b, target):
    a.sort() # O(nlogn)
    b.sort() # O(nlogn)

    i = 0
    j = len(b) - 1

    closest = [a[i], b[j]]
    closestDistance = getDistanceToTarget(target, closest)

    # O(n)
    while i < len(a) and j > 0:
        currentSum = a[i] + b[j]

        if currentSum == target:
            return [a[i], b[j]]

        if currentSum < target:
            i += 1
        
        if currentSum > target:
            j -= 1

        currentDistance = abs(target - currentSum)

        if currentDistance < closestDistance:
            closestDistance = currentDistance
            closest = [a[i], b[j]]

    return closest

def getDistanceToTarget(target, values):
    if values is None:
        return float('inf')

    x, y = values
    return abs(target - x - y)

if __name__ == "__main__":
    a = [-1, 3, 8, 2, 9, 5]
    b = [4, 1, 2, 10, 5, 20]
    target = 24
    res = closestSumInArrays(a, b, target)
    print(res)
