class Solution(object):
    
    def getRoot(self, start, uSet):
        if uSet[start] == -1: return -1
        else:
            while uSet[start] != -2:
                start = uSet[start]
        return start
    
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        uSet = [-1] * n
        for temp in edges:
            lroot = self.getRoot(temp[0], uSet)
            rroot = self.getRoot(temp[1], uSet)
            if lroot == -1 and rroot == -1:
                uSet[temp[0]] = -2
                uSet[temp[1]] = temp[0]
            elif lroot == -1:
                uSet[temp[0]] = rroot
            elif rroot == -1:
                uSet[temp[1]] = lroot
            else:
                if lroot != rroot:
                    uSet[rroot] = lroot
        res = 0
        for temp in uSet:
            if temp < 0: res += 1
        return res
