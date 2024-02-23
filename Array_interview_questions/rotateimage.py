"""
Input: matrix = [[1,2,3],
                [4,5,6],
                [7,8,9]]
Output: [[7,4,1],
        [8,5,2],
        [9,6,3]]       
"""

class Solution:
    
    def rotate(self, matrix: list[list[int]]):
        n = len(matrix)
        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()

        return matrix
    


ss = Solution()
matrix = [[1,2,3],
        [4,5,6],
        [7,8,9]]
print(ss.rotate(matrix=matrix))