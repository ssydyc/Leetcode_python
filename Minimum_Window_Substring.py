class Solution:
    # @return a string
    def minWindow(self, S, T):
        dict_T={}
        for x in T:
            if x in dict_T:
                dict_T[x]+=1
            else:
                dict_T[x]=1
        len_T=len(dict_T) # the number we need
        num_match=0 # record the number of match
        min_window=[0,0,0] # record the index and minimum size
        visited={} #dictionary to record the visited letters
        for x in T:
            visited[x]=0 #initialize it
        if T=='': return ''
        begin,end=-1,-1 #record the place of string containing
        for x in S:
            end+=1
            if x in T:
                visited[x]+=1
                if visited[x]==dict_T[x]: num_match+=1 
                if num_match==len_T: #now we have a new one
                    while num_match==len_T:
                        begin+=1
                        if S[begin] in T:
                            visited[S[begin]]-=1
                            if visited[S[begin]]<dict_T[S[begin]]: num_match-=1
                        # adjust the begin part
                    if min_window[2]==0 or min_window[2]>end-begin+1:
                        min_window=[begin-1,end,end-begin+1] #we have a window
                    #now adjust the begin part
        if min_window[2]==0: return ''
        else: return S[min_window[0]+1:min_window[1]+1]
                
