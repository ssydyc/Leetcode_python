'''
Created on Jan 20, 2014

@author: songsi
'''

class Solution:
    def twoSum(self, numbers, target):
        hashmap={}
        for head in range(0,len(numbers)):
            if target-numbers[head] in hashmap:
                tail=hashmap[target-numbers[head]]
                break
            else:
                hashmap[numbers[head]]=head
            
        result=[]
        result.append(tail+1)
        result.append(head+1)
        return result
        
test=Solution()
print test.twoSum([3,2,4],6)