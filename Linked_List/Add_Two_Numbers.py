# Add Two Numbers

'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.


Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummyHead = ListNode(0)  # dummyHead will hold the resulting linked list.
        tail = dummyHead  # the pointer tail will keep track of the last node in the result list. 
        carry = 0

        # start the loop that continues until there are no more digits in both input lists and there is no remaining carry value.
        while l1 or l2 or carry != 0: 
            digit1 = l1.val if l1 else 0  # 2
            digit2 = l2.val if l2 else 0  # 5

            Sum = digit1 + digit2 + carry  # 7
            digit = Sum % 10  # 7
            carry = Sum // 10  # 0

            newNode = ListNode(digit)  # 7 
            tail.next = newNode  # attach the new node to the tail node of the result list.
            tail = tail.next  # move the tail pointer to the newly added node.

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None

        result = dummyHead.next  # obtain the actual result list by skipping the dummyHead node.
        dummyHead.next = None  # delete the dummyHead node.
        return result
