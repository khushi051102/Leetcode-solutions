class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        rows,cols=len(matrix),len(matrix[0])
        top,bottom=0,rows-1
        left,right=0,cols-1
        flatten=[]

        while top<=bottom and left<=right:
            for c in range(left,right+1):
                flatten.append(matrix[top][c])
            top+=1

            for r in range(top,bottom+1):
                flatten.append(matrix[r][right])
            right-=1

            if top<=bottom:
                for c in range(right,left-1,-1):
                    flatten.append(matrix[bottom][c])
                bottom-=1

            if left<=right:
                for r in range(bottom,top-1,-1):
                    flatten.append(matrix[r][left])
                left+=1
        
        return flatten