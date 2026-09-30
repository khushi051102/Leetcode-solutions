class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        n,m=len(matrix),len(matrix[0])
        zero_rows,zero_cols=set(),set()

        for i in range(n):
            for j in range(m):
                if matrix[i][j]==0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        for i in range(n):
            for j in range(m):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j]=0