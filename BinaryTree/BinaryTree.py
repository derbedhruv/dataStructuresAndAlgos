"""
Implementation of a Binary Tree

The following methods have been implemented:
* 

AUTHOR: Dhruv Joshi
"""
import sys, math
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
  def __init__(self, L):
    # create a binary tree from an
    # array representation of the same
    # An element of None will represent a null node
    # 'n' is the index of the element on the list
    # i.e. our current 'root' is the n'th element (1-indexed)
    # first convert the list to length 2^n by appending the 
    # requisite number of None elements to the end
    L += [None]*(len(L) - 2**int(math.log(len(L), 2)))

    def createFromListInternal(L, n=1):
      if 2*n+1 >= len(L):
        return None
      root = BinaryTreeNode(val=L[n-1])
      root.left = createFromListInternal(L, n=2*n)
      root.right = createFromListInternal(L, n=2*n+1)
      return root

    self.root = createFromListInternal(L)
    self.numElements = len(L)

  def display(self):
    # pretty print the binary tree on terminal
    # do not print NULL values
    printStack = []   # stack for printing, keep appending to this

    # convert all the keys to string (if not None)
    # and pad with spaces to make them of the same length (== max(all lengths))


    def displayLine(lineNum):
      # print a single line of nodes
      # print space if there's a NULL node
      pass



