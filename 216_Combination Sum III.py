class Solution(object):
    def helper(self, k, n, res, candidate):
        if k == 0:
            if n == 0: res.append(list(candidate))
            return
        lastAdd = candidate[-1] if candidate else 0
        for i in range(lastAdd + 1, 10):
            if i <= n:
                candidate.append(i)
                self.helper(k - 1, n - i, res, candidate)
                candidate.pop()
        
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []
        candidate = []
        self.helper(k, n, res, candidate)
        return res
