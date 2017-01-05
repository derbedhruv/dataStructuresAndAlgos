'''
	DEPTH FIRST SEARCH IMPLEMENTATION IN PYTHON
'''
import sys
sys.path.append("../graph/")
sys.path.append("../stack")

from graph import GraphNode, Graph
from stack import Stack, Queue

def graphSearch(graph, startNode, verbose, datatype):
	# generalized graph search
	# given data structure (stack/queue), it will run the same process
	pipeline = datatype()	# create a new instance of the passed datatype
	# We start by putting the startNode in the pipeline
	# TODO: handle the case when the startNode is not in the graph!
	pipeline.push(startNode.key)
	explored = []

	# Begin the search
	# Pop from pipeline, see if the element has been explored
	# If not, add to explored list and add its children to the pipeline
	while(pipeline.isEmpty() == False):
		# pop from pipeline
		current_node = graph.nodes[pipeline.pop()]
		if current_node in explored:
			continue

		if verbose:
			print "Exploring", current_node.key
		explored.append(current_node)
		for child in graph.adjacency_list[current_node]:
			# add all children to the pipeline
			pipeline.push(child.key)
	return

def dfs(graph, startNode, verbose=False):
	# --------------------------------------------------------- #
	# Depth-first search on graphs			   					#
	# ---------------------------------------------------------	#
	# Depth first search will be performed on graph, starting	#
	# from the node given as argument.
	# In this case, it will simply print out the elements as it #
	# traverses them if verbose is true							#
	# ---------------------------------------------------------	#
	return graphSearch(graph=graph, startNode=startNode, verbose=verbose, datatype=Stack)


def bfs(graph, startNode, verbose=False):
	# --------------------------------------------------------- #
	# Breadth-first search on graphs		   					#
	# ---------------------------------------------------------	#
	# Breadth first search will be performed on graph, starting	#
	# from the node given as argument.
	# In this case, it will simply print out the elements as it #
	# traverses them. 											#
	# ---------------------------------------------------------	#
	return graphSearch(graph=graph, startNode=startNode, verbose=verbose, datatype=Queue)
