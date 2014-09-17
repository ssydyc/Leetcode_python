class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    result=[]
    temp_result=[]
    candidates=[]

    def combinationSum(self, candidates, target):
        candidates=list(set(candidates))
        self.candidates=sorted(candidates)
        if len(candidates)==0:
            return self.result
        self.my_combination(target,0)
        return self.result[0:1]

    def my_combination(self, target, current):
    # current is the number of candidates we need to test
        if target==0:
            self.result.append(self.temp_result)
            self.temp_result=list(self.temp_result)
            self.temp_result.pop()
        else:
            for i in range(current,len(self.candidates)):
                if self.candidates[i]<=target:
                    target=target-self.candidates[i]
                    self.temp_result.append(self.candidates[i])
                    self.my_combination(target,i)
                    target=target+self.candidates[i]
            if len(self.temp_result)!=0:
                self.temp_result.pop()

test=Solution()
print test.combinationSum([1],2)