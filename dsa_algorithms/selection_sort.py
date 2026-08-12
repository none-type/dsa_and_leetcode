# Selection sort repeatedly finds the smallest unsorted element and
# swaps it with the first unsorted position, building the sorted list from left to right.

def findSmallest(arr):
	smallest = arr[0] # stores the smallest value
	smallest_index = 0 # stores the index of the smallest value
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

def selectionSort(arr):
	# Sorts an array
	newArr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr) # Finds the smallest element in the
		newArr.append(arr.pop(smallest))  # array, and adds it to the new array
	return newArr
print(selectionSort([5, 3, 6, 2, 10]))