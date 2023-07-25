#!/usr/bin/env python3

"""35.

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4

Constraints:

    1 <= nums.length <= 10^4
    -10^4 <= nums[i] <= 10^4
    `nums` contains distinct values sorted in ascending order.
    -10^4 <= target <= 10^4
"""

examples = [([1, 3, 5, 6], 5, 2), ([1, 3, 5, 6], 2, 1), ([1, 3, 5, 6], 7, 4)]


class Solution:
    def binary_search(self, nums: list[int], left: int, right: int, target: int) -> int:
        while left < right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle

            if nums[middle] < target:
                left = middle + 1
            else:
                right = middle

            return self.binary_search(nums, left, right, target)

        return left

    def searchInsert(self, nums: list[int], target: int) -> int:
        print(f"Searching for index of {target} in {nums}")
        return self.binary_search(nums, 0, len(nums), target)

    def test_examples(self):
        for e in examples:
            assert self.searchInsert(e[0], e[1]) == e[2]


if __name__ == "__main__":
    Solution().test_examples()

# Runtime Details 65ms Beats 58.53%of users with Python3 || Memory Details 17.16mb Beats 56.72%of users with Python3
