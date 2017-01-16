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
	swapped = True

	while(swapped == True):
		swapped = False
		for j in range(1, n):
			if array[j] < array[j-1]:
				swap(j,j-1)
				swapped = True

	# return array
	return array