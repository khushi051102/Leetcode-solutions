class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        row=[1]
        for c in range(1,rowIndex+1):
            nextvalue=row[-1]*(rowIndex-c+1)//c
            row.append(nextvalue)
        return row
