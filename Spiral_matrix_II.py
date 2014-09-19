class Solution:
    # @return a list of lists of integer
    def generateMatrix(self, n):
        matrix=[[0 for i in range(n)] for j in range(n)] # generate n*n matrix
        if n==0: return []
        cur_x=0 #starting point
        cur_y=-1
        value=0
        while n>0:
            #go to right
            for i in range(n):
                cur_y+=1
                value+=1
                matrix[cur_x][cur_y]=value
            #go to bottom
            for i in range(n-1):
                cur_x+=1
                value+=1
                matrix[cur_x][cur_y]=value
            #go t left
            for i in range(n-1):
                cur_y-=1
                value+=1
                matrix[cur_x][cur_y]=value
            for i in range(n-2):
                cur_x-=1
                value+=1
                matrix[cur_x][cur_y]=value
            n-=2
        return matrix
