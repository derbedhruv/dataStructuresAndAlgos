'''
	SINGLY LINKED LIST IMPLEMENTATION IN PYTHON

	Singly linked list with basic methods implemented as python class. 
	Depends on the Node class - which can take any single element as its key value.
'''
# create Node class
class Node:
	# ---------------------------------------- #
	# Node class 							   #
	# ---------------------------------------- #
	# A node has the following attributes:	   #
	#   * value - a single element (any type)  #
	#   * next - a pointer to a Node 		   #
	# ---------------------------------------- #
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

class Linkedlist:
	# ---------------------------------------- #
	# Singly linked list class				   #
	# ---------------------------------------- #
	# A linked list is a collection of nodes,  #
	# which are chained together in one 	   #
	# direction. They have the following	   #
	# attributes:							   #
	#   * startNode - a pointer to the first   #
	#   node is the chain 					   #
	#										   #
	# They have the following methods:		   #
	#   * insert() - inserts a new Node at the #
	#     end of the linked list 			   #
	# 	* display() - pretty print linked list #
	#	* delete() - deletes the Node in the   #
	#	  linked list specified by a pointer   #
	# ---------------------------------------- #
	def __init__(self, startNode = None):
		self.startNode = startNode

	def insert(self, nextNode):
		# keep looping till you reach the end and then insert
		current_Node = self.startNode
		if (current_Node != None):
			while(current_Node.next != None):
				current_Node = current_Node.next

			current_Node.next = nextNode
		else:
			self.startNode = nextNode

	def display(self):
		current_Node = self.startNode
		if (current_Node == None):
			return

		while(current_Node != None):
			print(current_Node.value), "->",
			current_Node = current_Node.next
		print "NULL"

	def delete(self, pointer):
		# pointer is a pointer to the node that has to be deleted
		# Will do a scan from the start - O(n) time complexity unfortunately
		if self.startNode == pointer:
			self.startNode = self.startNode.next
			return
		current_Node = self.startNode
		if (current_Node != None):
			while(current_Node.next != None):
				if (current_Node.next != pointer):
					current_Node = current_Node.next
				else:
					break

		current_Node.next = pointer.next

	def isEmpty(self):
		# check for linked list being empty by checking if
		# startNode is None. Used in stacks and queues
		if self.startNode == None:
			return True
		else:
			return False

	def reverse(self):
		# reverse the linkedlist in-situ
		# initialize pointers
		P1 = None
		P2 = self.startNode
		P3 = P2.next
		def incrementPointers(P1, P2, P3):
			# simple function to increment the pointers
			P1 = P2
			P2 = P3
			P3 = P3.next
			return (P1, P2, P3)
		# Now begin the while loop
		while (P3 != None):
			# make the second node in the window point to the first
			P2.next = P1
			P1, P2, P3 = incrementPointers(P1, P2, P3)
		P2.next = P1
		self.startNode = P2



if __name__ == "__main__":
	## Interview practice question: will code up a linkedlist which has two types of elements and then use the "runner" approach to change the nodes to alternate between each type
	count = 2
	type1 = [0 for _ in range(count)]
	type2 = ['x' for _ in range(count)]

	L = Linkedlist()

	# insert first type of element
	for t1 in type1:
		L.insert(Node(t1))

	for t2 in type2:
		L.insert(Node(t2))

	print "First linked list:"
	L.display()

	# Now we will apply the runner method
	pointer1 = L.startNode
	pointer2 = L.startNode

	while(pointer2 != None):
		pointer1 = pointer1.next

		for _ in range(2):
			pointer2 = pointer2.next

	# Now the second pointer is at the end and the first one is at the middle, now re-shuffle
	# Move pointer2 to the start again, and advance pointer1 to the first node of the second type
	# and do a pass through the whole linked list
	pointer2 = L.startNode

	while(True):
		temp = pointer2.next
		pointer2.next = pointer1
		pointer2 = temp

		temp = pointer1
		pointer1 = pointer1.next
		if (pointer1 == None):
			temp.next = None
			break
		temp.next = pointer2

	L.display()


	## Second interview questoin - removing duplicates in a linked list
	LL = Linkedlist()
	LL.insert(Node(0))
	LL.insert(Node(1))
	LL.insert(Node(0))

	splnode = Node(11)
	LL.insert(splnode)
	LL.display()
	LL.delete(splnode)
	LL.display()



