# Reorder List

'''
You are given the head of a singly linked-list. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.

Example:
Input: head = [1,2,3,4,5]
Output: [1,5,2,4,3]
'''

'''
For list [1,2,3,4,5,6,7] we need to return [1,7,2,6,3,5,4]. We can note, that it is actually two lists [1,2,3,4] and [7,6,5], where elements are interchange. So, to succeed we need to do the following steps:

1. Find the middle of or list - be careful, it needs to work properly both for even and for odd number of nodes. For this we can either just count number of elements and then divide it by to, and do two traversals of list. Or we can use slow/fast iterators trick, where slow moves with speed 1 and fast moves with speed 2. Then when fast reches the end, slow will be in the middle, as we need.

2. Reverse the second part of linked list. Again, if you never done it before, it can be quite painful, please read oficial solution to problem 206. Reverse Linked List. The idea is to keep three pointers: prev, curr, nextt stand for previous, current and next and change connections in place. Do not forget to use slow.next = None, in opposite case you will have list with loop.

3. Finally, we need to merge two lists, given its heads. These heads are denoted by head and prev, so for simplisity I created head1 and head2 variables. What we need to do now is to interchange nodes: we put head2 as next element of head1 and then say that head1 is now head2 and head2 is previous head1.next. In this way we do one step for one of the lists and rename lists, so next time we will take element from head2, then rename again and so on.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # step 1: find middle
        if not head: return []
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # step 2: reverse second half
        prev, curr = None, slow.next
        while curr:
            nextt = curr.next
            curr.next = prev
            prev = curr
            curr = nextt
        slow.next = None
        # For example, for list [1,2,3,4,5,6], slow.next = None breaks it into [1,2,3] and [6,5,4]. Otherwise, we have [1,2,3,4] and [6,5,4], which results in a cycle in step 3.

        # step 3: merge lists
        head1, head2 = head, prev
        while head2:
            nextt = head1.next
            head1.next = head2
            head1 = head2
            head2 = nextt
