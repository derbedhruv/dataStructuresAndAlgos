'''
	DEPTH FIRST SEARCH IMPLEMENTATION IN PYTHON
'''
import sys
sys.path.append("../graph/")
sys.path.append("../stack")

from graph import GraphNode, Graph
from stack import Stack

def dfs(graph, startNode):
	# --------------------------------------------------------- #
	# Depth-first search on graphs			   					#
	# ---------------------------------------------------------	#
	# Depth first search will be performed on graph, starting	#
	# from the node given as argument.
	# In this case, it will simply print out the elements as it #
	# traverses them. 											#
	# ---------------------------------------------------------	#
	stack = Stack()
	# We start by putting the startNode in the stack
	# TODO: handle the case when the startNode is not in the graph
	stack.push(startNode.key)
	explored = []

	# Then we begin looping
	# Check for stack being non-empty
	# Emptiness is checked by seeing if the startNode of the 
	# underlying linked list is None (empty linked list)
	while(stack.isEmpty() == False):
		# pop from stack
		current_node = graph.nodes[stack.pop()]
		if current_node in explored:
			continue

		# print current_node.key, ":", [n.key for n in graph.adjacency_list[current_node]]
		print "Exploring", current_node.key
		explored.append(current_node)
		for child in graph.adjacency_list[current_node]:
			# add all children to the stack
			stack.push(child.key)
	return
