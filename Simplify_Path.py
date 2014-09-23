class Solution:
    # @param path, a string
    # @return a string
    def simplifyPath(self, path):
        path=path.split('/')
        result=[''] #add one for root
        for temp in path:
            if temp=='..':
                if len(result)!=1:
                    result.pop()
            elif temp=='.' or temp=='':
                pass
            else:
                result.append(temp)
        if len(result)==1: return '/'
        else: return '/'.join(result)
