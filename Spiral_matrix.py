class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        m=len(matrix) #record the current level
        if m==0: return []
        n=len(matrix[0])
        cur_x=0 #starting point
        cur_y=-1
        result=[]
        while m>0 and n>0:
            #go to right
            move=True
            for i in range(n):
                cur_y+=1
                result.append(matrix[cur_x][cur_y])
            #go to bottom
            if m==1: move=False
            if move:
                for i in range(m-1):
                    cur_x+=1
                    result.append(matrix[cur_x][cur_y])
            #go t left
            if n==1: move=False
            if move:
                for i in range(n-1):
                    cur_y-=1
                    result.append(matrix[cur_x][cur_y])
                for i in range(m-2):
                    cur_x-=1
                    result.append(matrix[cur_x][cur_y])
            m-=2
            n-=2
        return result
