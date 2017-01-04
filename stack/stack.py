'''
	STACK and QUEUE IMPLEMENTATION IN PYTHON

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
	#   * pop - removes last element		   #
	#   * push - inserts new last element      #
	#	* isEmpty - returns True if empty 	   #
	# ---------------------------------------- #
	def pop(self):
		try:
			pop_value = self.startNode.value
			self.startNode = self.startNode.next
			return pop_value
		except AttributeError:
			# empty stack
			return None

	def push(self, newval):
		newNode = Node(value=newval, next=self.startNode)
		self.startNode = newNode

	def isEmpty(self):
		# check for stack being empty by checking if
		# startNode of underlying linked list is None
		if self.startNode == None:
			return True
		else:
			return False


# Queue implementation
class Queue(Linkedlist):
	# -------------------------------------------------	#
	# A FIFO buffer							   			#
	# ------------------------------------------------- #
	# Define the following methods:			   			#
	#   * add() - adds an item to the end of the queue  #
	# 	* remove() - removes and returns the first item #
	# ------------------------------------------------- #
	def add(self, newval):
		self.insert(Node(newval))

	def remove(self):
		try:
			first_in_queue = self.startNode.value
			self.delete(self.startNode)
			return first_in_queue
		except AttributeError:
			# empty queue
			return None