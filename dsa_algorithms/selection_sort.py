# Selection sort repeatedly finds the smallest unsorted element and
# swaps it with the first unsorted position, building the sorted list from left to right.
# Big O for selection sort is O(n**2)

# you don’t have to check a list of n elements each time.
# You check n elements, then n – 1, n - 2 … 2, 1. On average, you check a
# list that has 1/ 2 × n elements. The runtime is O(n × 1/ 2 × n). But constants
# like 1/2 are ignored in Big O notation (again, see chapter 4 for the full
# discussion), so you just write O(n × n) or O(n2 ).

def findSmallest(arr):
	smallest = arr[0] # stores the smallest value
	smallest_index = 0 # stores the index of the smallest value
	for i in range(1, len(arr)):
		print(f"findSmallest loop iteration {i}")
		if arr[i] < smallest: # smallest used for comparison only. smallest_index will be returned
			smallest = arr[i]
			smallest_index = i
	return smallest_index

def selectionSort(arr):
	# Sorts an array
	newArr = []
	for i in range(len(arr)):
		print(f"selectionSort loop iteration {i}")
		smallest = findSmallest(arr) # Finds the smallest element in the array
		newArr.append(arr.pop(smallest))  # removes it and adds it to the new array
	return newArr
print(selectionSort([5, 3, 6, 2, 10]))