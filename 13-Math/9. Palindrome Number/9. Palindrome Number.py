class Solution:
    def isPalindrome(self, n: int) -> bool:
        if n<0:
            return False
        original = n  
        rev = 0
        while n >0:
            digit = n% 10
            rev = rev * 10 + digit
            n //= 10 
        return original==rev


        