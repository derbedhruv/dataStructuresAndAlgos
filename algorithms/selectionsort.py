def selectionsort(array):
	# --------------------------------------------------------- #
	# Selection sort on arrays (of ints)		   				#
	# ---------------------------------------------------------	#
	# Will perform selection sort and return the sorted array	#
	# Input is a list of ints									#
	# ---------------------------------------------------------	#
	# The swap subroutine
	def swap(i, j):
		# Swaps the i'th and j'th elements of "array"
		array[i], array[j] = array[j], array[i]

	# begin the sorting process..
	n = len(array)
	for i in range(n):
		currentMin = array[i]
		currentMinIndex = i

		# keep scanning till you find minimum of the array elements in array[i+1:]
		for j in range(i+1, n):
			if array[j] < currentMin:
				currentMin = array[j]
				currentMinIndex = j

		# swap the min with the i'th element
		swap(i, currentMinIndex)

	return array