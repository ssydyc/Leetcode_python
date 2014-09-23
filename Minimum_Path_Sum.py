class Solution:
    # @param grid, a list of lists of integers
    # @return an integer
    def minPathSum(self, grid):
        if grid==None: return 0
        m,n=len(grid),len(grid[0])
        prev_row=[None]*n
        cur_row=[None]*n #define the default row
        for i in range(m):
            for j in range(n):
                if i!=0:
                    cur_row[j]=prev_row[j]+grid[i][j]
                if j!=0:
                    if cur_row[j]==None:
                        cur_row[j]=cur_row[j-1]+grid[i][j]
                    else:
                        cur_row[j]=min(cur_row[j],cur_row[j-1]+grid[i][j])
                if i==0 and j==0:
                    cur_row[j]=grid[i][j]
            cur_row,prev_row=prev_row,cur_row
        return prev_row[n-1]
