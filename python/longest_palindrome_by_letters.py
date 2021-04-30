class Solution:
    def longestPalindrome(self, s: str) -> int:
        chars = {}
        for char in s:
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
        total = 0
        haveOddCount = False
        for count in chars.values():
            haveOddCount = haveOddCount or count % 2 == 1
            total += (count // 2) * 2
        return total + 1 if haveOddCount else total

if __name__ == "__main__":
    s = "abccccdd"
    sol = Solution()
    print(sol.longestPalindrome(s))