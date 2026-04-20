"""
Docstring for Binary_Tree_ADT.tree
"""

from collections import deque

class Node:

    """
    Binary Tree ADT
    """

    def __init__(self, data, left = None, right = None):
        self.left = left
        self.right = right
        self.val = data

class BinaryTree:

    """
    Docstring for BinaryTree
    """

    def __init__(self):
        self.root = None

    def insert(self, value):

        """
        Docstring for insert
        """

        new_node = Node(value)
        if self.root is None:
            self.root = new_node

        else:
            queue = deque([self.root])
            while queue:
                current = queue.popleft()
                if not current.left:
                    current.left = new_node
                    break

                queue.append(current.left)
                if not current.right:
                    current.right = new_node
                    break

                queue.append(current.right)

    def delete(self, value):

        """
        Docstring for delete
        """

        if self.root is None:
            print("Tree is empty")
            return

        # Find the node to delete and the last node
        queue = deque([self.root])
        node_to_delete = None
        last_node = None
        parent_of_last_node = None

        while queue:
            current = queue.popleft()
            if current.left:
                queue.append(current.left)
                parent_of_last_node = current  # Update the parent reference
            if current.right:
                queue.append(current.right)
                parent_of_last_node = current  # Update the parent reference

            if current.val == value:
                node_to_delete = current
            last_node = current  # Update the last node reference

        if node_to_delete:
            # Replace the node to delete with the last node's value
            if last_node and node_to_delete != last_node:
                node_to_delete.val = last_node.val

            # Remove the last node from the tree
            if parent_of_last_node:
                if parent_of_last_node.right == last_node:
                    parent_of_last_node.right = None

                elif parent_of_last_node.left == last_node:
                    parent_of_last_node.left = None

    def search(self, value):

        """
        Docstring for search
        """

        if not self.root:
            return "Tree is empty"

        queue = deque([self.root])
        while queue:
            current = queue.popleft()

            if current.val == value:
                return f"Value {value} found in the tree"

            if current.left:
                queue.append(current.left)

            if current.right:
                queue.append(current.right)

        return f"Value {value} not found in the tree"

class BST:

    """
    Docstring for BST
    """

    def __init__(self):
        self.root = None

    def insert(self, value):

        """
        Docstring for insert
        """

        if self.root is None:
            self.root = Node(value)

        else:
            self._insert(self.root, value)

    def _insert(self, node, value):
        if value < node.val:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(node.right, value)

    def search(self, value):

        """
        Docstring for search
        """

        return self._search(self.root, value)

    def _search(self, node, value):

        if node is None:
            return f"Value {value} not found in the tree"

        if value == node.val:
            return f"Value {value} found in the tree"

        if value < node.val:
            return self._search(node.left, value)

        return self._search(node.right, value)
