# ========================================
# SLIDING WINDOW
# ========================================

# Extension of 2 pointer. Manages a range of values = window.
# Inspec or process a segment.
# Like dragging a scanner accross a line of text.
# Reduces time complexity to o(n)
# Fixed and dynamic windows.

# With a fixed window, it removes one element from left,
# and adds on to the right.

# FIXED WINDOW PSEUDO CODE
# ------------------------

# def sliding_window_fixed(input, window_size):
# 	ans = window = input[0: window_size]

# 	for right in range(window_size, len(input)):
# 		left = right - window_size
# 		remove input[left] from window
# 		append input[right] to window
# 		ans = optimal(ans, window)
# 	return ans

# DYNAMIC WINDOW PSEUDO CODE
# ------------------------

# def sliding_window_flexible_longest(input):
# 	initialize window, ans
# 	left = 0
# 	for right in range(len(input)):
# 		append input[right] to window
# 		while invalid(window):
# 			remove input[left] from window  
# 			left += 1 	
# 		ans = max(ans, window)
# 	return ans 
# 	

def subarray_sum_fixed(nums: list[int], k: int)-> int:
	window_sum = 0
	for i in range(k):
		window_sum += nums[i]
	largest = window_sum
	for right in range(k, len(nums)):
		left = right - k
		window_sum -= nums[left]
		window_sum += nums[right]
		largest = max(largest, window_sum)
	return largest

if __name__ == "__main__":
	nums = [list(x) for x in input().split()]
	k = int(input())
	res = subarray_sum_fixed(nums, k)
	print(res)