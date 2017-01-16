def bubblesort(array):
	# --------------------------------------------------------- #
	# Bubble sort on arrays (of ints)		   					#
	# ---------------------------------------------------------	#
	# Will perform bubble sort and return the sorted array		#
	# Input is a list of ints									#
	# ---------------------------------------------------------	#
	# The swap subroutine
	def swap(i, j):
		# Swaps the i'th and j'th elements of "array"
		array[i], array[j] = array[j], array[i]

	# Now run through the list n times and swap adjacent
	n = len(array)
	for i in range(n):
		for j in range(i+1, n):
			swap(i,j)

	# return array
	return array