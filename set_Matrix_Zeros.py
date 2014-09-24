class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        rows=set([])
        columns=set([])
        if len(matrix)==0: return
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    rows.add(i)
                    columns.add(j)
        for temp in rows:
            matrix[temp]=[0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in columns:
                matrix[i][j]=0
        return
