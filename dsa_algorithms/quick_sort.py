# Quick Sort - picks pivot, partitions (left < pivot < right), recursively sorts
# In-place sorting, good for memory

def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition returns pivot index where left < pivot < right
        pivot_idx = partition(arr, low, high)
        
        # Recursively sort left and right halves
        quick_sort(arr, low, pivot_idx - 1)
        quick_sort(arr, pivot_idx + 1, high)
    
    return arr

def partition(arr, low, high):
    # Choose rightmost as pivot
    pivot = arr[high]
    i = low - 1  # Index of smaller element
    
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]  # Swap
    
    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Example
arr = [3, 6, 8, 10, 1, 2, 1]
print("Quick sort:", quick_sort(arr.copy()))  # [1, 1, 2, 3, 6, 8, 10]