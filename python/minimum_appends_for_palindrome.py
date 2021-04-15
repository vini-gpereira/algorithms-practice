class Solution:
    # @param A : string
    # @return an integer
    def solve(self, A):
        n = len(A)
        i = 0
        j = n - 1
        equals = 0
        diff = 0

        while i < j:
            if A[i] != A[j]:
                diff += 1 + equals
                equals = 0
                j = n - 1
            else:
                j -= 1
                equals += 1
            i += 1

        return diff

if __name__ == "__main__":
    sol = Solution()
    print(sol.solve("oqycntornscygodzdctxnhoc"))
