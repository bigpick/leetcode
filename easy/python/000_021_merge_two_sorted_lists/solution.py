#!/usr/bin/env python3

"""21. Merge two sorted lists
You are given the heads of two sorted linked lists `list1` and `list2`.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.
"""

from __future__ import annotations
from typing import Optional
from copy import deepcopy


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: Optional[ListNode] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val=}, {self.next=})"

    def __eq__(self, __value: object) -> bool:
        if not self:
            return False if __value else True

        if not __value:
            return False if self else True

        if self.val != __value.val:
            return False

        n = self.next
        n2 = __value.next

        while n and n2:
            if n.val != n2.val:
                return False

            n = n.next
            n2 = n2.next

        return n == n2


ListNodeInputOutput = tuple[Optional[ListNode], Optional[ListNode], Optional[ListNode]]
examples: list[ListNodeInputOutput] = [
    (None, None, None),
    (None, ListNode(0, None), ListNode(0, None)),
    (ListNode(3, None), ListNode(2, None), ListNode(2, ListNode(3, None))),
]


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        merged = prev = ListNode()

        if not list1 and not list2:
            return None

        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next

        if list1:
            prev.next = list1
        if list2:
            prev.next = list2

        return merged.next

    def test_examples(self):
        for e in examples:
            c = deepcopy(e)
            print(self.mergeTwoLists(c[0], c[1]))
            assert self.mergeTwoLists(e[0], e[1]) == e[2]


if __name__ == "__main__":
    Solution().test_examples()

# Runtime 57 ms Beats 22.62% || Memory 16.3 MB Beats 61.60%
