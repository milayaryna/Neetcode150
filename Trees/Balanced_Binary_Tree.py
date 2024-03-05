# Balanced Binary Tree

'''
Given a binary tree, determine if it is height-balanced.
A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true
'''

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        # If either subtree is unbalanced or the difference in heights is greater than 1, the tree root is unbalanced.
        def dfs(root):
            if not root:
                return [True, 0]

            # Recursive calls for left and right subtrees
            left, right = dfs(root.left), dfs(root.right)

            # Check if the current tree is balanced and update height
            balanced  = (left[0] and right[0] and abs(left[1] - right[1]) <= 1) # The difference in heights (abs(0 - 1)) is less than or equal to 1, so the subtree is balanced.

            # Return [balanced, height]
            return [balanced, 1 + max(left[1], right[1])]

        # Call the dfs function and return the result
        return dfs(root)[0]
