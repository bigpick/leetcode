#!/usr/bin/env python3

"""28. Find the Index of the First Occurrence in a String

Given two strings needle and haystack, return the index of the first
occurrence of needle in haystack, or -1 if needle is not part of
haystack.
"""

examples = [("sadbutsad", "sad", 0), ("leetcode", "leeto", -1)]


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            return haystack.index(needle)
        except ValueError:
            return -1

    def test_examples(self):
        for e in examples:
            assert self.strStr(e[0], e[1]) == e[2]


if __name__ == "__main__":
    Solution().test_examples()

# Runtime 45 ms Beats 51.76% || Memory 16.2 MB Beats 55.9%
