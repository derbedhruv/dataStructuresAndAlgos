"""
Class definition for generic Node, which is used
to construct trees.

AUTHOR: Dhruv Joshi
"""

class Node:
  def __init__(self, values):
    # the pointer to the Node
    # the node has a dictionary of values
    # this ensures that the data structure is
    # extensible.
    self.val = values
