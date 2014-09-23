class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        to_add=1
        for i in range(len(digits)-1,-1,-1):
            digits[i]+=to_add
            to_add=0
            if digits[i]>9:
                digits[i]-=10
                to_add=1
        if to_add==1: digits.insert(0,1)
        return digits
