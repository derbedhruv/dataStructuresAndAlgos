'''
	STACK CLASS IMPLEMENTATION IN PYTHON

	Will implement using a singly linked list, extending the class written previously
'''
import sys
sys.path.append("../linkedlists/")

from linked_list import Linkedlist, Node

# Now we create a stack class which extends this
class Stack(Linkedlist):
	# ---------------------------------------- #
	# A LIFO buffer							   #
	# ---------------------------------------- #
	# Define the following methods:			   #
	#   * pop() - removes last element		   #
	#   * push() - inserts new last element    #
	# ---------------------------------------- #
	def pop(self):
		pop_value = self.startNode.value
		self.startNode = startNode.next
		return pop_value

	def push(self, newval):
		newNode = Node(value=newval, next=self.startNode)
		self.startNode = newNode