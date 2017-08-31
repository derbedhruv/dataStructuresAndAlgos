# Class for implementing a binary tree node
'''
class BinaryTreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
'''

class Node:
	def __init__(self, key, left=None, right=None):
		self.key = key
		self.left = left
		self.right = right

class BinaryTree:
	def __init__(self, startNode=None, sortedList=None):
		def median(l):
			# finds the median of a SORTED list l
			n = len(l)
			if n%2 == 0:
				return (n/2 - 1, l[n/2 - 1])
			else:
				return (n/2, l[n/2])
		def tree(l):
			# converts a sorted list l into a binary tree and returns the reference to the head node
			if len(l) == 0:
				return
			i, med = median(l)
			node = Node(med)
			node.left = tree(l[:i])
			node.right = tree(l[i+1:])
			return node

		if startNode != None:
			self.startNode = startNode
		if sortedList != None:
			self.startNode = tree(sortedList)


	def display(self):
		# print out the nodes (all in a line for now)
		def disp(l):
			child_list = []
			for ll in l:
				try:
					print ll.key,
					child_list += [ll.left, ll.right]
				except AttributeError:
					print ' ',
			print
			if len(child_list) != 0:
				disp(child_list)
			return

		disp([self.startNode])

# A readymade binary tree
if __name__ == "__main__":
	o = Node(3)
	n = Node(7)
	m = Node(8)
	l = Node(9)
	k = Node(1)
	j = Node(4)
	i = Node(2)
	h = Node(5)

	g = Node(9, left=n, right=o)
	f = Node(6, left=l, right=m)
	e = Node(3, left=j, right=k)
	d = Node(1, left=h, right=i)
	c = Node(7, left=f, right=g)
	b = Node(2, left=d, right=e)
	a = Node(4, left=b, right=c)

	x = BinaryTree(a)
	x.display()