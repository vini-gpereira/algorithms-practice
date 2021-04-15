class Solution:
    # @param A : tuple of integers
    # @return an integer
    def maxSubArray(self, A):
        s = 0
        maxSum = A[0]
        for num in A:
            s += num
            maxSum = max(s,maxSum)
            if s < 0:
                s = 0
        return maxSum

if __name__ == "__main__":
    sol = Solution()
    A = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(sol.maxSubArray(A))
