# Class for implementing a binary tree node
class BinaryTreeNode:
	def __init__(self, val, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right

class Node:
	def __init__(self, key, left=None, right=None):
		self.key = key
		self.left = left
		self.right = right

class BinaryTree:
	def __init__(self, startNode=Node(key=None)):
		self.startNode = startNode

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