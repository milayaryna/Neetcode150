# Remove Nth Node From End of List

'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

Example 1:
Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]

Example 2:
Input: head = [1], n = 1
Output: []

Example 3:
Input: head = [1,2], n = 1
Output: [1]
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head

        # advance fast to nth position
        for i in range(n):
            fast = fast.next
        # then both fast and slow are nth positions apart

        if not fast:
            return head.next
        # This handles the case where we are deleting the head from the linked list. In that case fast will have traversed the entire linked list. So fast is now null. Then obviously to snip the head, we just return head.next.

        while fast.next:
            slow = slow.next
            fast = fast.next
        # when fast gets to None, slow will be just before the item to be deleted

        # delet the node
        slow.next = slow.next.next
        return head
