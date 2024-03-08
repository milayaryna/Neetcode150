# Binary Tree Right Side View

'''
Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

Example 1:
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]

Example 2:
Input: root = [1,null,3]
Output: [1,3]

Example 3:
Input: root = []
Output: []
'''

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        q = collections.deque([root]) # Initialize a deque with the root node

        while q:
            rightMost = None
            
            # In the latest loop, rightMost will be the right-most node at the current level.
            for i in range(len(q)):
                node = q.popleft()
                if node:
                    rightMost = node
                    q.append(node.left)
                    q.append(node.right)
            
            if rightMost:
                result.append(rightMost.val)

        return result
