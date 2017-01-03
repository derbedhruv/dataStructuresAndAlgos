'''
	SINGLY LINKED LIST IMPLEMENTATION IN PYTHON
'''
# create Node class
class Node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

class Linkedlist:
	def __init__(self, startNode):
		self.startNode = startNode

	def insert(self, nextNode):
		# keep looping till you reach the end and then insert
		current_Node = self.startNode
		while(current_Node.next != None):
			current_Node = current_Node.next

		current_Node.next = nextNode

	def display(self):
		current_Node = self.startNode
		while(current_Node.next != None):
			print(current_Node.value), "->",
			current_Node = current_Node.next
		print "NULL"


a = Node(5)
a.next = Node(7)
print a.next.value


b = Linkedlist(a)
b.insert(Node(8))
b.display()