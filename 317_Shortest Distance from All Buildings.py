class Solution(object):
    def BFS(self, visited, start, grid):
        # return result as the center
        m, n = len(grid), len(grid[0])
        level = -1
        q = collections.deque([start])
        visited[start[0]][start[1]] = True
        res = 0
        while q:
            level += 1
            for i in range(len(q)):
                temp = q.popleft()
                if grid[temp[0]][temp[1]] == 0 or temp == start:
                    if temp[0] > 0 and not visited[temp[0] - 1][temp[1]]:
                        q.append((temp[0] - 1, temp[1]))
                        visited[temp[0] - 1][temp[1]] = True
                    if temp[0] < m - 1 and not visited[temp[0] + 1][temp[1]]:
                        q.append((temp[0] + 1, temp[1]))
                        visited[temp[0] + 1][temp[1]] = True
                    if temp[1] > 0 and not visited[temp[0]][temp[1] - 1]:
                        q.append((temp[0], temp[1] - 1))
                        visited[temp[0]][temp[1] - 1] = True
                    if temp[1] < n - 1 and not visited[temp[0]][temp[1] + 1]:
                        q.append((temp[0], temp[1] + 1))
                        visited[temp[0]][temp[1] + 1] = True
                elif grid[temp[0]][temp[1]] == 1:
                    res += level
        return res
                
    def connected(self, visited, grid):
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if not visited[i][j] and grid[i][j] == 1:
                    return False
        return True
    
    def clear(self, visited):
        for i in range(len(visited)):
            for j in range(len(visited[0])):
                visited[i][j] = False
    
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        res = -1
        connect = False
        m, n = len(grid), len(grid[0])
        visited = [[False] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and not connect: # judge whether it's connected
                    temp = self.BFS(visited, (i,j), grid)
                    if not self.connected(visited, grid): return -1
                    connect = True
                elif grid[i][j] == 0:
                    temp = self.BFS(visited, (i,j), grid)
                    if temp != 0 and self.connected(visited, grid):
                        if res == -1: res = temp
                        else: res = min(res, temp)
                self.clear(visited)
        return res
