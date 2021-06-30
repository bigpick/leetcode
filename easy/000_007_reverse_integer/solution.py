class Solution:
    def reverse(self, x: int) -> int:
        l = list(str(x))
        val = 0

        if str(x)[0] == "-":
            val = int("-" + ''.join(l[1:][::-1]))
        else:
            val = int(''.join(l[::-1]))

        if abs(val) > pow(2, 31)-1:
            return 0
        else:
            return val
