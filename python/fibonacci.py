class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, n):
        if n == 1 or n == 2:
            return 1

        Q = [[1, 1], [1, 0]]
        Qfixed = [[1, 1], [1, 0]]
        res = self.matrixPower(Q, Qfixed, n - 1)
        return res[0][0] % 1000000007

    def matrixPower(self, M, C, n):
        if n == 1:
            return M
            
        H = self.matrixPower(M, C, n // 2)
        res = self.multiplyMatrices(H, H)

        if n % 2 == 1:
            res = self.multiplyMatrices(res, C)

        return res


    def multiplyMatrices(self, M1, M2):
        a11 = ((M1[0][0] * M2[0][0]) % 1000000007 + (M1[0][1] * M2[1][0]) % 1000000007) % 1000000007
        a12 = ((M1[0][0] * M2[0][1]) % 1000000007 + (M1[0][1] * M2[1][1]) % 1000000007) % 1000000007
        a21 = ((M1[1][0] * M2[0][0]) % 1000000007 + (M1[1][1] * M2[1][0]) % 1000000007) % 1000000007
        a22 = ((M1[1][0] * M2[0][1]) % 1000000007 + (M1[1][1] * M2[1][1]) % 1000000007) % 1000000007

        return [[a11, a12], [a21, a22]]
