'''
	SINGLY LINKED LIST IMPLEMENTATION IN PYTHON
'''
# create node class
class node:
	def __init__(self, value, next=None):
		self.value = value
		self.next = next

	def next(self):
		return next

	def value(self):
		return value


class linkedlist:
	def __init__(self, startnode):
		self.startnode = startnode

	def insert(self, nextnode):
		# keep looping till you reach the end and then insert
		current_node = self.startnode
		while(current_node.next != None):
			current_node = current_node.next

		current_node.next = nextnode

	def display(self):
		current_node = self.startnode
		while(current_node.next != None):
			print(current_node.value), "->",
			current_node = current_node.next
		print "NULL"


a = node(5)
a.next = node(7)
# print a.next.value


b = linkedlist(a)
b.insert(node(8))
b.display()