#!/usr/bin/env python3

"""58. Length of Last Word

Given a string s consisting of words and spaces, return the length of the last word in the string.

A word is a maximal `substring` consisting of non-space characters only.
"""

examples = [
    ("Hello World", 5),
    ("   fly me   to   the moon  ", 4),
    ("luffy is still joyboy", 6),
]


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split()[-1])

    def test_examples(self):
        for e in examples:
            assert self.lengthOfLastWord(e[0]) == e[1]


if __name__ == "__main__":
    Solution().test_examples()

# Runtime Details 46ms Beats 59.54%of users with Python3 || Memory Details 16.26mb Beats 88.52%of users with Python3
