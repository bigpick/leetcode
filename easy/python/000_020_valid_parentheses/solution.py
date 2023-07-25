#!/usr/bin/env python3

"""20. Valid Parentheses

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"
Output: true

Example 2:

Input: s = "()[]{}"
Output: true

Example 3:

Input: s = "(]"
Output: false

Constraints:

    1 <= s.length <= 104
    s consists of parentheses only '()[]{}'.
"""

POS_CASES = ["()", "()[]{}"]
NEGATIVE_CASES = ["(]"]


class Solution:
    def isValid(self, s: str) -> bool:
        openings = {"(", "[", "{"}
        pairings = {"}": "{", ")": "(", "]": "["}
        stack = []

        for c in s:
            if c in openings:
                stack.append(c)
            else:
                if len(stack) == 0 or pairings[c] != stack.pop():
                    return False

        return len(stack) == 0

    def test_examples(self):
        assert all([self.isValid(inp) for inp in POS_CASES])
        assert not any([self.isValid(inp) for inp in NEGATIVE_CASES])


if __name__ == "__main__":
    Solution().test_examples()

# Runtime49 ms Beats 26.95% || Memory16.4 MB Beats 6.29%
