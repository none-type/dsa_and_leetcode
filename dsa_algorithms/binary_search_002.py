# Binary Search - O(log n) time, O(1) space, works on SORTED arrays

# 1. ITERATIVE VERSION (most common)
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1   # Search right half
        else:
            right = mid - 1  # Search left half
    
    return -1  # Not found

# Example
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Index of 7:", binary_search(arr, 7))   # 6
print("Index of 11:", binary_search(arr, 11)) # -1

# 2. RECURSIVE VERSION
def binary_search_recursive(arr, target, left, right):
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

print("Recursive find 5:", binary_search_recursive(arr, 5, 0, len(arr)-1))  # 4

# 3. BINARY SEARCH VARIATIONS

# Find first occurrence (for duplicates)
def first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Keep searching left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

arr_dup = [1, 2, 2, 2, 3, 4]
print("First 2:", first_occurrence(arr_dup, 2))  # 1

# Find insertion position (where target should be)
def insertion_pos(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return left  # Insert position

print("Insert 5 at:", insertion_pos([1, 3, 5, 6], 5))   # 2
print("Insert 2 at:", insertion_pos([1, 3, 5, 6], 2))   # 1
print("Insert 7 at:", insertion_pos([1, 3, 5, 6], 7))   # 4

# 4. REAL-WORLD USE: Python's bisect module
import bisect
arr = [1, 3, 5, 7, 9]
print("Bisect left:", bisect.bisect_left(arr, 5))   # 2
print("Bisect right:", bisect.bisect_right(arr, 5)) # 3

# 5. SEARCH IN ROTATED SORTED ARRAY (advanced use)
def search_rotated(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        
        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

rotated = [4, 5, 6, 7, 0, 1, 2]
print("Find 0 in rotated:", search_rotated(rotated, 0))  # 4

# Common use cases: dictionary lookup, database queries, debugging with git bisect