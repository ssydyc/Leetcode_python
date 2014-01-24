'''
Created on Jan 22, 2014

@author: songsi
'''
class Solution:
    # @return an integer
    def threeSumClosest(self, num, target):
        num.sort()
        answer=num[0]+num[1]+num[2]
        for i in range(0,len(num)-2):
            #num[i] will be the first element
            target_2=target-num[i]
            head=i+1
            tail=len(num)-1
            while(tail>head):
                if num[head]+num[tail]==target_2:
                    return target
                elif num[head]+num[tail]>target_2:
                    if abs(answer-target)>abs(num[head]+num[tail]-target_2):
                        answer=num[head]+num[tail]+num[i]
                    tail-=1
                else:
                    if abs(answer-target)>abs(num[head]+num[tail]-target_2):
                        answer=num[head]+num[tail]+num[i]
                    head+=1
        return answer
    
test=Solution()
print test.threeSumClosest([-1,2,1,4], 1)