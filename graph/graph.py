'''
	IMPLEMENTATION OF GRAPH DATA STRUCTURE IN PYTHON
'''
from collections import defaultdict

class GraphNode:
	# --------------------------------------------------------- #
	# A Graph Node object					   					#
	# ---------------------------------------------------------	#
	# A graph node contains a values of any data type 			#
	# ---------------------------------------------------------	#
	def __init__(self, value):
		self.value = value

class Graph:
	# --------------------------------------------------------- #
	# A Graph object						   					#
	# ---------------------------------------------------------	#
	# A graph will be implemented as a defaultdict of lists of 	#
	# Node objects. The key will be the Node itself
	# It will have the following methods:
	# ---------------------------------------------------------	#
	def __init__(self, adjacency_list=defaultdict(list)):
		self.adjacency_list = adjacency_list

	def add_connection(self, node1, node2):
		# Adds a connection from node1 to node2 in the graph
		self.adjacency_list[node1].append(node2)

	def display(self):
		# Displays the graph in easily readable form
		for node in self.adjacency_list.keys():
			print node.value, ":", ' ,'.join([child_node.value for child_node in self.adjacency_list[node]])
