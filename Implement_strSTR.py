'''
Created on Jan 31, 2014

@author: songsi
'''
import time

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
    #kmp algorithm
    #create table first
        if needle=="": return haystack
        if haystack=="": return None
        table=[]
        i=0
        current=0
        while i<len(needle):
            if i==0:  
                table.append(-1)
                i+=1
            elif i==1: 
                table.append(0)
                i+=1
            else:
                if needle[i-1]==needle[current]:
                    current+=1
                    table.append(current)
                    i+=1
                else:
                    if current==0: 
                        table.append(0)
                        i+=1
                    else:
                        current=table[current]
        #now doing string match
        match_number=0
        current=0
        i=0
        while current+len(needle)-1<len(haystack):
            if haystack[current+match_number]==needle[match_number]:
                match_number+=1
                if match_number==len(needle): return haystack[current:]
            else:
                current+=match_number-table[match_number]
                if current+len(needle)-1>=len(haystack): return None
                match_number=max(table[match_number],0)
                
