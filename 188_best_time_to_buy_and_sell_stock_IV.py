class Solution:
    # @return an integer as the maximum profit 
    def quickProfit(self,prices):
        # when k is big, return profit
        result=0
        for i in range(len(prices)-1):
            if prices[i+1]-prices[i]>0:
                result+=prices[i+1]-prices[i]
        return result
    
    def maxProfit(self, k, prices):
        if k==0: return 0
        if k>len(prices)/2: return self.quickProfit(prices)
        global_cur=[0]*(k+1)
        global_next=[0]*(k+1)
        local_cur=[0]*(k+1)
        local_next=[0]*(k+1)
        for i in range(len(prices)-1):
            # do it n-1 times
            diff=prices[i+1]-prices[i]
            for j in range(1,k+1,1):
                # local_next[j] means util j
                local_next[j]=max(global_cur[j-1]+max(diff,0),local_cur[j]+diff)
                global_next[j]=max(global_cur[j],local_next[j])
            global_cur,global_next=global_next,global_cur
            local_cur,local_next=local_next,local_cur
        return global_cur[k]
