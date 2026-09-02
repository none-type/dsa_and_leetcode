# arrays are default ds for everything
# arrays give you conastant time access by index O(1) time
# arrays are stored contiguously in memory
# to insert or delete elements in the middle is slow O(n)
# appending at end, or access by index is fast O(1)

# what to use it for?
	# traverse a structure in order
	# access specific indices
	# compare elements from both ends
	# sliding window, prefix sum etc

# strings are arrays of characters
# strings are immutable
# if you modify a string, you are creating a new string
# concatenating strings in a loop is O(n**2)
# better to append to a empty list then join

# what are strings used for?
	# find the longest substring without repeating characters
	# check if two strings are anagrams
	# return all substrings that match a pattern
	# usually these are two pointer, or sliding window problems
	# string problems are never about brute force
	# string problems are about smart windowing, fast lookup, efficient traversal

# Array (list) - contiguous memory, O(1) random access

# 1. DECLARE & INITIALIZE
arr = [5, 2, 8, 1, 9]  # dynamic size in Python
print("Original:", arr)  # [5, 2, 8, 1, 9]

# 2. ACCESS - O(1)
print("Element at index 2:", arr[2])  # 8

# 3. SEARCH - O(n)
target = 1
index = arr.index(target) if target in arr else -1
print(f"Index of {target}:", index)  # 3

# 4. INSERT at end - O(1) amortized
arr.append(7)
print("After append:", arr)  # [5, 2, 8, 1, 9, 7]

# 5. INSERT at specific position - O(n)
arr.insert(2, 99)  # insert 99 at index 2
print("After insert at index 2:", arr)  # [5, 2, 99, 8, 1, 9, 7]

# 6. DELETE by value - O(n)
arr.remove(8)
print("After removing 8:", arr)  # [5, 2, 99, 1, 9, 7]

# 7. DELETE at index - O(n)
deleted = arr.pop(1)  # removes index 1 (value 2)
print(f"Popped {deleted}, array:", arr)  # [5, 99, 1, 9, 7]

# 8. SLICE - O(k) where k = slice length
sub = arr[1:4]  # [99, 1, 9]
print("Slice [1:4]:", sub)

# 9. ITERATE
for i, val in enumerate(arr):
    print(f"arr[{i}] = {val}")

# Common use: storing ordered data, matrix operations, buffer