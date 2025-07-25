class Solution:
    def reverse(self, x: int) -> int:
        ans = 0
        if x < 0:
            sign=-1 
        else:
            sign=1
        x *= sign
        while x:
            ans = ans * 10 + x % 10
            x //= 10
        if ans < -2**31 or ans > 2**31 - 1:
            return 0
        else:
            return sign * ans