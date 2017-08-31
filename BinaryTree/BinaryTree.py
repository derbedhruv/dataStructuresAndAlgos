"""
Implementation of a Binary Tree

The following methods have been implemented:
* 

AUTHOR: Dhruv Joshi
"""
import sys
sys.path.append("../Node")

from Node import Node

class BinaryTreeNode(Node):
  # extending the Node class 
  # https://stackoverflow.com/questions/12701206/how-to-extend-python-class-init
  def __init__(self, val=None, nextVal=None, prev=None):
    Node.__init__(self, val)
    self.next = nextVal
    self.prev = prev

class BinaryTree:
  def __init__(self, rootVal=None):
    # initialize a binary tree
    # point to the root node
    self.root = BinaryTreeNode(rootVal)

