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


# Queue implementation
class Queue(Linkedlist):
	# -------------------------------------------------	#
	# A FIFO buffer							   			#
	# ------------------------------------------------- #
	# Define the following methods:			   			#
	# <Named same as stack to make it easier to change	#
	#   * push - adds an item to the end of the queue  	#
	# 	* pop - removes and returns the first item 		#
	# ------------------------------------------------- #
	def push(self, newval):
		self.insert(Node(newval))

	def pop(self):
		try:
			first_in_queue = self.startNode.value
			self.delete(self.startNode)
			return first_in_queue
		except AttributeError:
			# empty queue
			return None