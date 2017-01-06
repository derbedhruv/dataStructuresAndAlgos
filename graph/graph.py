'''
	IMPLEMENTATION OF GRAPH DATA STRUCTURE IN PYTHON
'''
from collections import defaultdict
from operator import attrgetter

class GraphNode:
	# --------------------------------------------------------- #
	# A Graph Node object					   					#
	# ---------------------------------------------------------	#
	# A graph node contains a key of any data type	 			#
	# More attributes can be added later to make it a rich		#
	# collection of values about some object. 					#
	# ---------------------------------------------------------	#
	def __init__(self, key):
		self.key = key

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


class Graph:
	# --------------------------------------------------------- #
	# A Graph object						   					#
	# ---------------------------------------------------------	#
	# A graph will be implemented as a defaultdict of lists of 	#
	# Node objects. The key will be the value of a Nodes. 		#
	# We will also maintain a dict which maps keys to Nodes. 	#
	#															#
	# It has the following methods:
	#   * add_connection: Adds a connection between two Nodes 	#
	# 	  identified by their key values. If nodes corresponding#
	#	  to either of these keys do not exist, they are created#
	#	  and added to the graph.
	#	* display: Pretty prints the graph
	#	* remove_connection: removes a connection between two	#
	#	  elements. If they do not exist, simply returns false. #
	# ---------------------------------------------------------	#
	def __init__(self, adjacency_list=defaultdict(list), directed=True):
		self.directed = directed
		self.adjacency_list = adjacency_list
		self.nodes = {}
		for node in adjacency_list:
			self.nodes[node.key] = node

	def add_connection(self, key1, key2):
		# Adds a connection from val1 to val2 in the graph.
		# First will check if nodes corresponding to these keys exist.
		# If they do not, it will create new nodes corresponding to them and add a connection between the two.
		# It will also return False if so.
		#
		# If the graph is a directed one (default), then it will make a one-way connection. 
		# Otherwise will make a two-way connection
		flag = True
		try:
			node1 = self.nodes[key1]
		except KeyError:
			node1 = GraphNode(key1)
			self.nodes[key1] = node1
			flag = False

		try:
			node2 = self.nodes[key2]
		except KeyError:
			node2 = GraphNode(key2)
			self.nodes[key2] = node2
			flag = False

		self.adjacency_list[node1].append(node2)
		if self.directed == False:
			self.adjacency_list[node1].append(node1)
		return flag

	def display(self):
		# Displays the graph in easily readable form
		for node in self.adjacency_list.keys():
			print node.key, ":", ', '.join([str(child_node.key) for child_node in self.adjacency_list[node]])

	def remove_connection(self, node1, node2):
		# Removes a connection in the graph by removing an element node2 from the list corresponding to node1
		# If it fails (i.e. if either of the nodes do not exist), returns False
		try:
			self.adjacency_list[node1].remove(node2)
			if self.directed == False:
				self.adjacency_list[node2].remove(node1)
			return True
		except:
			return False
