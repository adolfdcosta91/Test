# Types of Binary Tree

# Full Binary Tree
# This tree every node other than leaf nodes has 2 child nodes.


# Complete Binary Tree
# Fill all the nodes from the far left as possible


# Perfect Binary Tree
# All nodes should have 2 child nodes and all the leaf nodes should be one same level

# Degenerant Binary Tree
# Every node should have only 1 child node.
#
#
# class Node:
#
#     def __init__(self, data):
#
#         self.left = None
#         self.right = None
#         self.data = data
#
#     def insert(self, data):
#         if self.data:
#             if self.left is None:
#                 self.left = Node(data)
#
#             else:
#                 self.left.insert(data)
#
#             if self.right is None:
#                 self.right = Node(data)
#             else:
#                 self.right.insert(data)
#         else:
#             self.data=data
#
#
#     def PrintTree(self):
#         if self.left:
#             self.left.PrintTree()
#         print( self.data),
#         if self.right:
#             self.right.PrintTree()
#
#
# root = Node(12)
# root.insert(13)
# root.insert(18)
# root.insert(21)
#
# root.PrintTree()
#



# Another way to impliment binary tree using library

print("Impliment Binary tree using library")

import binarytree

Node = [2,5,4,6,8,10,12,14,16,18]

Tree = binarytree.build(Node)

print(Tree)
