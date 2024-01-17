# Reverse Linked List

'''
Given the head of a singly linked list, reverse the list, and return the reversed list.
Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None  # initialize prev pointer as Null
        curr = head  # initialize curr pointer as the head

        # run a loop till curr points to Null
        while curr:
            temp = curr.next  # initialize temp pointer as the next pointer of curr
            curr.next = prev  # assign the prev pointer to curr's next pointer
            prev = curr  # assign curr to prev, next to curr
            curr = temp
        return prev
