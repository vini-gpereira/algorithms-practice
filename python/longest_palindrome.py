class Solution:
    # @param A : string
    # @return a strings
    def longestPalindrome(self, A):
        n = len(A)
        
        if n <= 1:
            return A
        
        maxPalStart = 0
        maxPalEnd = 0

        for i in range(n):
            j = n - 1
            while j >= i:
                if self.isPalindrome(A, i, j) and j - i + 1 > maxPalEnd - maxPalStart + 1:
                    maxPalStart = i
                    maxPalEnd = j
                j -= 1
            if n - i < maxPalEnd - maxPalStart + 1:
                break

        return A[maxPalStart:(maxPalEnd + 1)]
        
    def isPalindrome(self, s, start, end):
        i = start
        j = end
        
        while i < j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        
        return True
        
if __name__ == "__main__":
    string = "ac"
    solution = Solution()
    palindrome = solution.longestPalindrome(string)
    print(palindrome)