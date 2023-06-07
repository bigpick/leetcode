class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = min(strs, key=len)
        longest_common = ""

        for idx, char in enumerate(shortest):
            for word in strs:
                if word[idx] != char:
                    return longest_common
            longest_common += char

        # Case where they pass us nothing
        return longest_common
