'''
	IMPLEMENTATION OF GRAPH DATA STRUCTURE IN PYTHON
'''
from collections import defaultdict

class GraphNode:
	# --------------------------------------------------------- #
	# A Graph Node object					   					#
	# ---------------------------------------------------------	#
	# A graph node contains a key of any data type	 			#
	# More attributes can be added later to make it a rich		#
	# collection of values about some object. 					#
	# ---------------------------------------------------------	#
	def __init__(self, value):
		self.key = value

class Graph:
	# --------------------------------------------------------- #
	# A Graph object						   					#
	# ---------------------------------------------------------	#
	# A graph will be implemented as a defaultdict of lists of 	#
	# Node objects. The key will be the value of a Nodes. 		#
	# We will also maintain a dict which maps keys to Nodes. 	#
	#															#
	# It will have the following methods:
	# ---------------------------------------------------------	#
	def __init__(self, adjacency_list=defaultdict(list)):
		self.adjacency_list = adjacency_list
		self.nodes = {}
		for node in adjacency_list:
			self.nodes[node.key] = node

	def add_connection(self, key1, key2):
		# Adds a connection from val1 to val2 in the graph.
		# First will check if nodes corresponding to these keys exist.
		# If they do not, it will create new nodes corresponding to them and add a connection between the two.
		# It will also return False if so.
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
			return True
		except:
			return False