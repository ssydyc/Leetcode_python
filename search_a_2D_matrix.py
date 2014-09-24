class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        #2D binary search
        if len(matrix)==0: return False
        m=len(matrix)
        n=len(matrix[0])
        top=0
        bottom=m-1
        while top<bottom:
            if matrix[(top+bottom)/2][0]==target: return True
            elif matrix[(top+bottom)/2][0]>target:
                bottom=(top+bottom)/2-1
            else:
                top=(top+bottom)/2
                if matrix[top+1][0]>target:
                    bottom-=1
                else:
                    top+=1
        sear_row=top
        if matrix[sear_row][0]==target: return True

        top=0
        bottom=n-1 #search row now
        while top<bottom:
            if matrix[sear_row][(top+bottom)/2]==target: return True
            elif matrix[sear_row][(top+bottom)/2]>target:
                bottom=(top+bottom)/2-1
            else:
                top=(top+bottom)/2+1
        if matrix[sear_row][top]==target: return True
        return False
