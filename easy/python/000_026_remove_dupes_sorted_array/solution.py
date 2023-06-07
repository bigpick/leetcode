#!/usr/bin/env python3

"""26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the
duplicates in-place such that each unique element appears only once. The
relative order of the elements should be kept the same. Then return the
number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted,
you need to do the following things:

    Change the array nums such that the first k elements of nums contain
    the unique elements in the order they were present in nums initially.
    The remaining elements of nums are not important as well as the size
    of nums.

    Return k.

Custom Judge:

The judge will test your solution with the following code:

```
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation

assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
```

If all assertions pass, then your solution will be accepted.
"""

examples = [
    ([1, 1, 2], [1, 2], 2),
    ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4], 5),
]


class CustomJudge:
    def __init__(self, given: list[int], expected: list[int], expected_k: int) -> None:
        self.expected = expected
        self.expected_k = expected_k
        self.given = given

    def validate(self):
        removed = Solution().removeDuplicates(self.given)
        assert self.expected_k == removed
        assert self.expected == self.given


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        correct = 1

        for i in range(len(nums) - 1, 0, -1):
            if nums[i] == nums[i - 1]:
                del nums[i]
            else:
                correct += 1

        return correct

    def test_examples(self):
        for e in examples:
            judge = CustomJudge(e[0], e[1], e[2])
            judge.validate()


if __name__ == "__main__":
    Solution().test_examples()

# Runtime 108 ms Beats 29.86% || Memory 18.1 MB Beats 12.71%
