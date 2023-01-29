"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

"""

"""NOTE:

Linked List looks like: ListNode{val: 7, next: ListNode{val: 0, next: ListNode{val: 8, next: None}}}

"""

# Official Solution

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)
        curr = dummyHead
        carry = 0
        while l1 != None or l2 != None or carry != 0:
            l1Val = l1.val if l1 else 0
            l2Val = l2.val if l2 else 0
            columnSum = l1Val + l2Val + carry
            carry = columnSum // 10
            newNode = ListNode(columnSum % 10)
            curr.next = newNode
            curr = newNode
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummyHead.next


# My Solution

"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        resultList = ListNode(0)
        currentNode = resultList
        while l1 != None or l2 != None or carry != 0:
            val1 = l1.val if l1 != None else 0
            val2 = l2.val if l2 != None else 0

            valSum = val1 + val2 + carry
            valDigit = valSum % 10
            carry = valSum // 10

            currentNode.val = valDigit

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

            if(l1 == None and l2 == None and carry == 0):
                currentNode.next = None
            else:
                currentNode.next = ListNode(0)
            currentNode = currentNode.next
        print(resultList)
        return resultList
"""