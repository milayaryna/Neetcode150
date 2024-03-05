# Invert Binary Tree

'''
Example 1:
Input: root = [4,2,7,1,3,6,9]
Output: [4,7,2,9,6,3,1]

Example 2:
Input: root = [2,1,3]
Output: [2,3,1]

Example 3:
Input: root = []
Output: []
'''

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        # swap the children
        root.left, root.right = root.right, root.left

        # make two recursive calls
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root
