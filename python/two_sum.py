from random import randint

def twoSum(nums, target):
    n = len(nums)
    for i in range(0, n - 2):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return None

def twoSumHash(nums, target):
    m = {}
    for i in range(len(nums)):
        num = nums[i]
        if num in m:
            return [m[num], i]
        else:
            complement = target - num
            m[complement] = i
    return None

if __name__ == "__main__":
    nums = [randint(1, 100) for _ in range(10)]
    expected = [randint(0, 9), randint(0, 9)]
    target = nums[expected[0]] + nums[expected[1]]
    result = twoSum(nums, target)
    print("Nums:", nums)
    print("Target:", target)
    print("Expect:", expected)
    print("Result:", result)

