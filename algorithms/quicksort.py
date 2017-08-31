import random

def quicksort(array, first, last):
	# --------------------------------------------------------- #
	# Quick sort on arrays (of ints)			   				#
	# ---------------------------------------------------------	#
	# Will perform quicksort and return the sorted arrays		#
	# Input is a list of ints									#
	# sorts in-place (no extra memory overhead)
	# ---------------------------------------------------------	#
	# The swap subroutine
	def swap(i, j):
		# Swaps the i'th and j'th elements of "array"
		array[i], array[j] = array[j], array[i]


	# base case
	n = last - first + 1
	if n <= 1:
		return

	def pivot(arr, first, last):
		# pivot around the last element - change to random element
		p = arr[last]
		i = first
		for j in range(first, last):
			if arr[j] <= pivot:
				swap(i, j)
		swap(i, p)
		return i

	# re-arrange elements around pivot into two new arrays
	p = pivot(array, first, last)

	# Now call quicksort on the two smaller arrays
	quicksort(array, first, p-1)
	quicksort(array, p+1, last)