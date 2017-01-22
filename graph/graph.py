'''
	IMPLEMENTATION OF GRAPH DATA STRUCTURE IN PYTHON
'''
# import stack and use it to return shortest path
import os, sys
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), "..", "stack/"))

from stack import Stack
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

	def add_connection(self, key1, key2, distance=1):
		# Adds a connection from val1 to val2 in the graph.
		# First will check if nodes corresponding to these keys exist.
		# If they do not, it will create new nodes corresponding to them and add a connection between the two.
		# It will also return False if so.
		#
		# If the graph is a directed one (default), then it will make a one-way connection. 
		# Otherwise will make a two-way connection
		#
		# distance represents the distance between the two nodes, default 1 unit

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

		self.adjacency_list[node1].append((node2, distance))
		if self.directed == False:
			self.adjacency_list[node2].append((node1, distance))
		return flag

	def display(self):
		# Displays the graph in easily readable form
		for node in self.adjacency_list.keys():
			print node.key, ":", ', '.join([str(child_node[0].key) for child_node in self.adjacency_list[node]])

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

	def shortest_path(self, sourcekey, targetkey):
		# --------------------------------------------------------- #
		# Implements Dijkstra's algorithm to find the shortest path #
		# from the source to target									#
		# Make sure that no path lengths are negative!				#
		# --------------------------------------------------------- #
		# get the actual pointers to the nodes
		# TODO: deal with case where the keys are not in the graph
		# TODO: How to handle multiple similar keys? OR assert unique keys
		source = self.nodes[sourcekey]
		target = self.nodes[targetkey]

		path = {}	# will be a dict of stacks keeping track of the shortest path till node
		unvisited_nodes = [self.nodes[node] for node in self.nodes]

		# tentative_distance keeps track of current lowest tentative distance from 'source' to each node
		# we set the distance to the source to be 0, and +inf for all others
		tentative_distance = {}
		tentative_distance[source] = 0
		for node in self.nodes:
			if self.nodes[node] != source:
				tentative_distance[self.nodes[node]] = float('+inf')

		# start exploring nodes, starting with the source
		while (len(unvisited_nodes) != 0):
			# update current_node to the one with the smallest tentative_distance (will be source itself at start)
			_, current_node = min((tentative_distance[unvisited_node], unvisited_node) for unvisited_node in unvisited_nodes)

			# get list of neighbours
			neighbours = self.adjacency_list[current_node]

			# compute updated tentative distances of neighbours
			for neighbourTuple in neighbours:
				# 'neighbourTuple' is a tuple of (node, distance_to_node) from current_node
				# see add_connection method
				# print "checking neightbour", neighbourTuple[0].key, "of node", current_node.key
				distance = neighbourTuple[1]
				newTentativeDistance = tentative_distance[current_node] + distance

				if tentative_distance[neighbourTuple[0]] > newTentativeDistance:
					# update hte tentative distance with the smaller one
					tentative_distance[neighbourTuple[0]] = newTentativeDistance

					# the shortest path to this node is through the current node
					path[neighbourTuple[0].key] = current_node.key

			# remove current_node from the unvisited set
			unvisited_nodes.remove(current_node)

		'''
		print "tentative distances from", sourcekey
		for n in tentative_distance:
			print n.key, ":", tentative_distance[n]
		'''
		# reverse traverse the shortest path, add to stack
		final_path = Stack()
		node = targetkey
		final_path.push(targetkey)

		while node != sourcekey:
			final_path.push(path[node])
			node = path[node]

		final_path.display()
		# return the shortest path from source to target
		return (final_path, tentative_distance[target])

