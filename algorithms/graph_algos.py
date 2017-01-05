'''
	DEPTH FIRST SEARCH IMPLEMENTATION IN PYTHON
'''
import sys
sys.path.append("../graph/")
sys.path.append("../stack")

from graph import GraphNode, Graph
from stack import Stack, Queue

def dfs(graph, startNode, verbose=False):
	# --------------------------------------------------------- #
	# Depth-first search on graphs			   					#
	# ---------------------------------------------------------	#
	# Depth first search will be performed on graph, starting	#
	# from the node given as argument.
	# In this case, it will simply print out the elements as it #
	# traverses them if verbose is true							#
	# ---------------------------------------------------------	#
	stack = Stack()
	# We start by putting the startNode in the stack
	# TODO: handle the case when the startNode is not in the graph
	stack.push(startNode.key)
	explored = []

	# Begin the search
	# Pop from stack, see if the element has been explored
	# If not, add to explored list and add its children to the stack
	while(stack.isEmpty() == False):
		# pop from stack
		current_node = graph.nodes[stack.pop()]
		if current_node in explored:
			continue

		if verbose:
			print "Exploring", current_node.key
		explored.append(current_node)
		for child in graph.adjacency_list[current_node]:
			# add all children to the stack
			stack.push(child.key)
	return


def bfs(graph, startNode, verbose=False):
	# --------------------------------------------------------- #
	# Breadth-first search on graphs		   					#
	# ---------------------------------------------------------	#
	# Breadth first search will be performed on graph, starting	#
	# from the node given as argument.
	# In this case, it will simply print out the elements as it #
	# traverses them. 											#
	# ---------------------------------------------------------	#
	queue = Queue()
	# We start by putting the startNode in the stack
	# TODO: handle the case when the startNode is not in the graph
	queue.add(startNode.key)
	explored = []

	# Begin the search
	# Pop from stack, see if the element has been explored
	# If not, add to explored list and add its children to the stack
	while(queue.isEmpty() == False):
		# pop from queue
		current_node = graph.nodes[queue.remove()]
		if current_node in explored:
			continue

		if verbose:
			print "Exploring", current_node.key
		explored.append(current_node)
		for child in graph.adjacency_list[current_node]:
			# add all children to the queue
			queue.add(child.key)
	return
