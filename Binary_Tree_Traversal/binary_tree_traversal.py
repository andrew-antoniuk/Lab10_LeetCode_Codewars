"""
Docstring for Binary_Tree_Traversal.binary_tree_traversal
"""

class Node:
    def __init__(self, v):
        self.left = None
        self.right = None
        self.data = v

# Pre-order traversal
def pre_order(node):

    """
    Docstring for pre_order
    """

    nodes = []

    if node is None:
        return None

    # Visit Node
    nodes.append(node.data)

    # Traverse left subtree
    pre_order(node.left)

    # Traverse right subtree
    pre_order(node.right)

    return nodes

# In-order traversal
def in_order(node):

    """
    Docstring for in_order
    """

    nodes = []

    if node:
        # Traverse left subtree
        in_order(node.left)

        # Visit node
        nodes.append(node.data)

        # Traverse right subtree
        in_order(node.right)

    return nodes


# Post-order traversal
def post_order(node):

    """
    Docstring for post_order
    """

    return []
