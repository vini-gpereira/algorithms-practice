class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        numsLen = len(nums)
        write = 0

        while write < numsLen and nums[write] != 0:
            write += 1

        read = write + 1

        while read < numsLen:
            if nums[read] != nums[write]:
                nums[write], nums[read] = nums[read], nums[write]
                write += 1
            read += 1