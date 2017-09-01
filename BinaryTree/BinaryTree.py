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
  def __init__(self, val=None, left=None, right=None):
    Node.__init__(self, val)
    self.left = left
    self.right = right

class BinaryTree:
  def __init__(self, rootVal=None):
    # initialize a binary tree
    # point to the root node
    if rootVal == None:
      self.root = None
    else:
      self.root = BinaryTreeNode(rootVal)

  def createFromList(self, L):
    # create a binary tree from an
    # array representation of the same
    # An element of None will represent a null node
    # 'n' is the index of the element on the list
    # i.e. our current 'root' is the n'th element (1-indexed)
    def createFromListInternal(L, n=1):
      if 2*n+1 >= len(L):
        return None
      root = BinaryTreeNode(val=L[n-1])
      root.left = createFromListInternal(L, n=2*n)
      root.right = createFromListInternal(L, n=2*n+1)
      return root

    self.root = createFromListInternal(L)
