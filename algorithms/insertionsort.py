def insertionsort(array):
	# --------------------------------------------------------- #
	# Insertion sort on arrays (of ints)		   				#
	# ---------------------------------------------------------	#
	# Will perform insertion sort and return the sorted array	#
	# Input is a list of ints									#
	# ---------------------------------------------------------	#
	# The swap subroutine
	def swap(i, j):
		# Swaps the i'th and j'th elements of "array"
		array[i], array[j] = array[j], array[i]

	# begin the algorithm
	n = len(array)
	for i in range(1, n):
		j = i
		while array[j] < array[j-1] and j > 0:
			# keep swapping with previous element till it is not less than it
			swap(j, j-1)
			if j-1 >= 0:
				j -= 1
	return array