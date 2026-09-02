# Two Pointers - O(n) time, O(1) space, works on sorted arrays/strings

# 1. OPPOSITE ENDS (left + right)
# Find pair that sums to target
def two_sum_sorted(arr, target):
    left, right = 0, len(arr) - 1
    
    while left < right:
        curr_sum = arr[left] + arr[right]
        
        if curr_sum == target:
            return [left, right]
        elif curr_sum < target:
            left += 1   # Need bigger sum
        else:
            right -= 1  # Need smaller sum
    
    return [-1, -1]  # No pair found

arr = [1, 2, 3, 4, 5, 6]
print("Sum to 7:", two_sum_sorted(arr, 7))   # [1, 4] (2+5)
print("Sum to 10:", two_sum_sorted(arr, 10)) # [3, 4] (4+6)

# 2. SAME DIRECTION (fast + slow)
# Remove duplicates from sorted array (in-place)
def remove_duplicates(arr):
    if not arr:
        return 0
    
    slow = 0  # Points to last unique element
    
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]  # Place unique element
    
    return slow + 1  # New length

arr_dup = [1, 1, 2, 2, 3, 3, 4]
length = remove_duplicates(arr_dup)
print("After removing duplicates:", arr_dup[:length])  # [1, 2, 3, 4]

# 3. PALINDROME CHECK
def is_palindrome(s):
    left, right = 0, len(s) - 1
    
    while left < right:
        # Skip non-alphanumeric
        while left < right and not s[left].isalnum():
            left += 1
        while left < right and not s[right].isalnum():
            right -= 1
        
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

print("Is 'race a car' palindrome:", is_palindrome("race a car"))  # False
print("Is 'A man a plan a canal Panama':", is_palindrome("A man a plan a canal Panama"))  # True

# 4. MERGE TWO SORTED ARRAYS
def merge_sorted(arr1, arr2):
    i = j = 0
    result = []
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # Add remaining
    result.extend(arr1[i:])
    result.extend(arr2[j:])
    return result

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
print("Merged:", merge_sorted(arr1, arr2))  # [1, 2, 3, 4, 5, 6, 7, 8]

# 5. CONTAINER WITH MOST WATER
def max_area(heights):
    left, right = 0, len(heights) - 1
    max_water = 0
    
    while left < right:
        # Calculate area: width * min(height)
        width = right - left
        height = min(heights[left], heights[right])
        max_water = max(max_water, width * height)
        
        # Move smaller height inward (try to find taller)
        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print("Max water:", max_area(heights))  # 49

# 6. THREE SUM (opposite ends + fixed pointer)
def three_sum(nums, target=0):
    nums.sort()
    result = []
    
    for i in range(len(nums) - 2):
        # Skip duplicates for i
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left, right = i + 1, len(nums) - 1
        
        while left < right:
            curr_sum = nums[i] + nums[left] + nums[right]
            
            if curr_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                # Skip duplicates
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
    
    return result

nums = [-1, 0, 1, 2, -1, -4]
print("Three sum to 0:", three_sum(nums))  # [[-1, -1, 2], [-1, 0, 1]]

# 7. REVERSE ARRAY IN-PLACE
def reverse_array(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

arr = [1, 2, 3, 4, 5]
reverse_array(arr)
print("Reversed:", arr)  # [5, 4, 3, 2, 1]

# Real-world uses: substring searches, sorting algorithms, 
# array manipulation, optimization problems, collision detection