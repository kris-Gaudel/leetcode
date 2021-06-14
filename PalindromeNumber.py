class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        forward_x = (str_x[::1])
        rev_x = ans = (str_x[::-1])

        if forward_x == rev_x:
            return True
        else:
            return False
