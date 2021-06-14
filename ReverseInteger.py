class Solution:
    def reverse(self, x: int) -> int:
        str_x = str(abs(x))
        rev_x = int(str_x[::-1])
        if rev_x > ((2**31)-1):
            return 0
        if x < 0:
            return (rev_x*-1)
        return rev_x
