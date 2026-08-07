def findSmallest(arr):
	smallest = arr[0]
	smallest_index = 0
	for i in range(1, len(arr)):
		if arr[i] < smallest:
			smallest = arr[i]
			smallest_index = i
	return smallest_index

def selectionSort(arr):
	 # Sorts an array
	newArr = []
	for i in range(len(arr)):
		smallest = findSmallest(arr)
	 	# Finds the smallest element in the
	 	# array, and adds it to the new array
		newArr.append(arr.pop(smallest)) 
	return newArr
print(selectionSort([5, 3, 6, 2, 10]))