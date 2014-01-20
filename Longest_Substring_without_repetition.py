'''
Created on Jan 15, 2014

@author: songsi
'''

def lengthOfLongestSubstring(s):
    behind=front=0  
    max_length=0
    while front<len(s)-1:
        front+=1
        has_rep=0 #meanining no rep
        for i in range(front-1,behind-1,-1):
            if s[i]==s[front]:
                has_rep=1
                break
        if has_rep==0:
            pass
        else:
            if front-behind>max_length:
                max_length=front-behind
            behind=i+1
    if front-behind+1>max_length:
        max_length=front-behind+1        
    return max_length        
            
print lengthOfLongestSubstring("qopubjguxhxdipfzwswybgfylqvjzhar")