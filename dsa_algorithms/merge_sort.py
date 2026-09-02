# Merge Sort - divide array in half, recursively sort, merge sorted halves
# Predictable O(n log n), uses extra memory, stable sort

def merge_sort(arr):
    # Base case
    if len(arr) <= 1:
        return arr
    
    # Divide - split into halves
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Conquer - merge sorted halves
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    
    # Compare and merge smaller elements first
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Example
arr = [3, 6, 8, 10, 1, 2, 1]
print("Merge sort:", merge_sort(arr))  # [1, 1, 2, 3, 6, 8, 10]