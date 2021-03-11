def countingValleys(steps, path):
    # Write your code here
    valleys = 0
    level = 0
    lastLevel = 0
    for step in path:
        lastLevel = level
        if step == 'D':
            level -= 1
        else:
            level += 1
        if lastLevel < 0 and level == 0:
            valleys += 1
    return valleys


if __name__ == '__main__':
    steps = 2
    path = "DUDUDU"
    result = countingValleys(steps, path)
    print(result)
