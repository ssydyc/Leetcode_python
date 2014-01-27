class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[0][0]==1: return 0
        result=[]
        for i in range(len(obstacleGrid)):
            result.append([])
            for j in range(len(obstacleGrid[0])):
                result[i].append(0)
        result[0][0]=1
        for i in range(len(obstacleGrid)):
            for j in range(len(obstacleGrid[0])):
                if obstacleGrid[i][j]==1 or (i==0 and j==0): pass
                else:
                    temp=0
                    if i>=1:
                        temp+=result[i-1][j]
                    if j>=1:
                        temp+=result[i][j-1]
                    result[i][j]=temp
        return result[i][j]
                        
test=Solution()
print test.uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])           