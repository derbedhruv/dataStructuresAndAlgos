class Heap:
	# --------------------------------------------------------- #
	# A Heap (min or max)                                       #
	# --------------------------------------------------------- #
	# A min or max heap, specified during initialization. It 
	# will be implemented as a list of GraphNode objects (other)
	# object types can also be passed, but they MUST have an
	# attribute "key" which will be used to compare them.
	# 
	# Define the following methods:
	#   * check_property: An internal function which checks if 
	#	  the heap property has been maintained.
	#	* insert: insert a new element into the heap
	# --------------------------------------------------------- #
	def __init__(self, htype="min", node=GraphNode):
		# the comparison functions
		# return True if the 
		def minfunc(node_of_interest, comparison_node):
			if node_of_interest.key >= comparison_node.key:
				return (True, comparison_node)
			return (False, node_of_interest)
		def maxfunc(node_of_interest, comparison_node):
			if node_of_interest.key <= comparison_node.key:
				return (True, comparison_node)
			return (False, node_of_interest)

		self.node = GraphNode
		self.heap = []
		if htype == "min":
			self.comparison_func = minfunc
		else:
			self.comparison_func = maxfunc

	def parent(self, node_of_interest):
		# returns the parent node of the node specified
		# integer division is used
		# The children of node 'n' are 2n+1 and 2n+2 in a 0-indexed system.
		return self.heap[(self.heap.index(node_of_interest)-1)/2]

	def check_property(self, node_of_interest):
		if self.heap.index(node_of_interest) == 0:
			return True
		return self.comparison_func(node_of_interest, self.parent(node_of_interest))[0]

	def swap(self, node1, node2):
		# swaps the actual node pointers in self.heap
		self.heap[self.heap.index(node2)], self.heap[self.heap.index(node1)] = self.heap[self.heap.index(node1)], self.heap[self.heap.index(node2)]

	def bubble_up(self, node_of_interest, display):
		# start at the node of interest, and recursively enforce the heap property locally till it is globally enforced
		if self.check_property(node_of_interest) == False:
			# self.swap(node_of_interest, self.parent(node_of_interest))
			parent = self.parent(node_of_interest)
			self.heap[self.heap.index(node_of_interest)] = self.parent(node_of_interest)
			self.heap[self.heap.index(parent)] = node_of_interest
			if display==True:
				self.display()
			self.bubble_up(node_of_interest, display)
		return

	def bubble_down(self, node_of_interest, display):
		# checks if the node is not consistent than its two children
		# if so, it replaces them with the min/max of the two recursively
		# base case: if there are no children, return
		index = self.heap.index(node_of_interest)
		first_child_index = 2*index + 1
		if first_child_index > len(self.heap)-1:
			return

		# if there is only one child, compare with that
		if first_child_index == len(self.heap) - 1:
			comparison_child = self.heap[first_child_index]
		else:
			comparison_child = self.comparison_func(self.heap[first_child_index], self.heap[first_child_index+1])[1]

		# perform a swap if there is a mismatch
		if self.comparison_func(comparison_child, node_of_interest)[0] == False:
			child_index = self.heap.index(comparison_child)
			self.heap[self.heap.index(node_of_interest)] = comparison_child
			self.heap[child_index] = node_of_interest
			if display==True:
				self.display()
			self.bubble_down(node_of_interest, display)
		return

	def display(self):
		print [node.key for node in self.heap]

	def insert(self, keyval, display=False):
		newNode = self.node(keyval)
		self.heap.append(newNode)
		self.bubble_up(newNode, display=display)

	def extract(self, display=False):
		# extract the min/max element of the heap
		min_node = self.heap[0]

		# bring the last element to the head, run heap property
		self.heap[0] = self.heap[len(self.heap) - 1]
		self.heap = self.heap[:-1]	# truncate last element
		self.bubble_down(self.heap[0], display=display)

		# return the min node
		return min_node