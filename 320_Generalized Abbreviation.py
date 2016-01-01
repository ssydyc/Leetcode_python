class Solution(object):
    
    def generateAbbreviations(self, word):
        """
        :type word: str
        :rtype: List[str]
        """
        res = []
        for i in range(len(word)):
            if not res: 
                res.append([word[i]])
                res.append(['1'])
            else:
                for j in range(len(res)):
                    temp = list(res[j])
                    res[j].append(word[i])
                    if temp[-1].isdigit():
                        temp[-1] = str(int(temp[-1])+1)
                    else:
                        temp.append('1')
                    res.append(temp)
        for i in range(len(res)):
            res[i] = "".join(res[i])
        if not res: return [""]
        else: return res
        
