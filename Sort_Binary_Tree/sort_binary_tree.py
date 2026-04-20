"""
Docstring for Sort_Binary_Tree.sort_binary_tree
"""

from collections import deque

def tree_by_levels(node):

    """
    Docstring for tree_by_levels
    """

    levels = []

    if node is None:
        return levels

    queue = deque([node])

    while len(queue) != 0:
        cur = queue.popleft()
        levels.append(cur.value)

        if cur.left is not None:
            queue.append(cur.left)

        if cur.right is not None:
            queue.append(cur.right)

    return levels
