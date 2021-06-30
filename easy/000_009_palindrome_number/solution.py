class Solution:
    def isPalindrome(self, x: int) -> bool:
        strnum = str(x)

        for i in range((len(strnum))//2):
            if strnum[i] == strnum[len(strnum) - 1 - i]:
                continue
            else:
                return False

        return True
