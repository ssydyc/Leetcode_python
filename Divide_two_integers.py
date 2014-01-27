class Solution:
    # @return an integer
    def divide(self, dividend, divisor):
        dividend=long(dividend)
        divisor=long(divisor)
        if (dividend>0 and divisor<0) or (dividend<0 and divisor>0):
            if dividend<0:
                return int(-self.mydivide(-dividend, divisor))
            else:
                return int(-self.mydivide(dividend, -divisor))
        else:
            if dividend<0:
                return int(self.mydivide(-dividend, -divisor))
            else:
                return int(self.mydivide(dividend, divisor))
            
    def mydivide(self, dividend, divisor):
        if dividend==divisor: return 1
        if dividend<divisor: return 0
        temp_divisor=divisor
        result=long(1)
        while temp_divisor<<1 < dividend:
            result=result<<1
            temp_divisor=temp_divisor<<1
        return result+self.mydivide(dividend-temp_divisor,divisor)
    