import random

def quicksort(array):
	# --------------------------------------------------------- #
	# Quick sort on arrays (of ints)			   				#
	# ---------------------------------------------------------	#
	# Will perform quicksort and return the sorted arrays		#
	# Input is a list of ints									#
	# ---------------------------------------------------------	#
	# base case
	if len(array) <= 1:
		return array

	# choose pivot
	pivot = random.sample(array, 1)[0]

	# re-arrange elements around pivot into two new arrays
	smaller = []
	larger = []
	for element in array:
		if element < pivot:
			smaller.append(element)
		if element > pivot:
			larger.append(element)

	# Now call quicksort on the two smaller arrays
	sorted_smaller = quicksort(smaller)
	sorted_larger = quicksort(larger)

	return sorted_smaller + [pivot] + sorted_larger