"""
Docstring for Delete_Node_BST.delete_node_bst
"""

from typing import Optional
from Binary_Tree_ADT.trees import BST as TreeNode

class Solution:

    """
    Docstring for Solution
    """

    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:

        """
        Docstring for delete_node
        """

        def get_successor(curr):
            curr = curr.right
            while curr is not None and curr.left is not None:
                curr = curr.left

            return curr

        if root is None:
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)

        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:

            # node with 0 or 1  children
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            #  Node with 2 children
            succ = get_successor(root)
            root.val = succ.val
            root.right = self.deleteNode(root.right, succ.val)

        return root
