class Solution:
    def beautifulMat(self, mat):
        for i in range(5):
            for j in range(5):
                if mat[i][j] == 1:
                    rows = abs(i - 2)
                    cols = abs(j - 2)
                    return rows + cols
                
if __name__ == '__main__':
    mat = [[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 0, 0],[0, 0, 0, 1, 0],[0, 0, 0, 0, 0]]
    obj = Solution()
    print(obj.beautifulMat(mat))