"""
Docstring for Binary_Tree_Traversal.binary_tree_traversal
"""

class Node:

    """
    Binary Tree ADT
    """

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

    if node:
        nodes.append(node.data)
        nodes.extend(pre_order(node.left))
        nodes.extend(pre_order(node.right))

    return nodes

# In-order traversal
def in_order(node):

    """
    Docstring for in_order
    """

    nodes = []

    if node:
        nodes = in_order(node.left)
        nodes.append(node.data)
        nodes.extend(in_order(node.right))

    return nodes

# Post-order traversal
def post_order(node):

    """
    Docstring for post_order
    """

    nodes = []

    if node:
        nodes = post_order(node.left)
        nodes.extend(post_order(node.right))
        nodes.append(node.data)

    return nodes
