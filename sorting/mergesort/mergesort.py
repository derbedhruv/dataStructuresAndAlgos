'''
	MERGE SORT IMPLEMENTATION IN PYTHON
'''

def mergesort(array):
	# ---------------------------------------- #
	# Merge sort 							   #
	# ---------------------------------------- #
	# Takes an array and returns the sorted    #
	# version of it. Takes a list of ints. 	   #
	# Runs in O(nlogn) time and space O(n)	   #
	# ---------------------------------------- #

	def merge(a, b):
		# ---------------------------------------- #
		# Merge subroutine						   #
		# ---------------------------------------- #
		# Takes two sorted lists a and b and 	   #
		# returns a single sorted list 			   #
		# ---------------------------------------- #
		def lowest_candidate(p, q):
			return min((x, i) for i,x in enumerate([p, q]) if x != None)

		def element(x, countx):
			# returns next element in list and None if we are out of the list
			if countx < len(x):
				return x[countx]
			else:
				return None

		# increment pointers (counta, countb) to list elements of each sub-list passed to merge()
		counta = 0
		countb = 0
		merged_list = []
		for _ in range(len(a) + len(b)):
			candidate, i = lowest_candidate(element(a, counta), element(b, countb))
			merged_list.append(candidate)

			increment_a, increment_b = [1 if j == i else 0 for j in range(2)]
			counta += increment_a
			countb += increment_b

		return merged_list

	l = len(array)
	# BASE CASE: If the array is two elements or less then sort it in a trivial way
	if l == 2:
		return [min(array), max(array)]
	if l == 1:
		return array

	# NORMAL CASE: Recursively sort and merge
	# split the array into two parts
	first = array[:l/2]
	second = array[l/2:]

	# then run each through mergesort
	first_sorted = mergesort(first)
	second_sorted = mergesort(second)

	# Then merge the two
	return merge(first_sorted, second_sorted)