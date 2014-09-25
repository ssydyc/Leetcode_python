class Solution:
    # @param board, a list of lists of 1 length string
    # @param word, a string
    # @return a boolean
    def dfs(self,board,word,start,visited):
        if len(visited)==len(word): return True #we have enough visited
        i,j=start
        m,n=len(board),len(board[0])
        if i>0 and (i-1,j) not in visited and board[i-1][j]==word[len(visited)]:
            visited.add((i-1,j))
            if self.dfs(board,word,(i-1,j),visited): return True
        if i<m-1 and (i+1,j) not in visited and board[i+1][j]==word[len(visited)]:
            visited.add((i+1,j))
            if self.dfs(board,word,(i+1,j),visited): return True 
        if j>0 and (i,j-1) not in visited and board[i][j-1]==word[len(visited)]:
            visited.add((i,j-1))
            if self.dfs(board,word,(i,j-1),visited): return True
        if j<n-1 and (i,j+1) not in visited and board[i][j+1]==word[len(visited)]:
            visited.add((i,j+1))
            if self.dfs(board,word,(i,j+1),visited): return True
        visited.remove((i,j))
        return False
    
    def exist(self, board, word):
        #do it with dfs
            if len(word)==0: return True
            if len(board)==0: return False #boundary case
            visited=set([]) #define a visited set
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j]==word[0]:
                        visited.clear()
                        visited.add((i,j))
                        if self.dfs(board,word,(i,j),visited): return True
            return False
                    
