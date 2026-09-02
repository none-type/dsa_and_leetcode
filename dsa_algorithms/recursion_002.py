# Recursion - function calls itself with smaller subproblem
# Key: Base case (stop) + Recursive case (reduce problem)

# 1. CLASSIC: FACTORIAL
def factorial(n):
    # Base case
    if n <= 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    return n * factorial(n - 1)

print("5! =", factorial(5))  # 120

# 2. CLASSIC: FIBONACCI
def fibonacci(n):
    # Base cases
    if n <= 0:
        return 0
    if n == 1:
        return 1
    # Recursive: fib(n) = fib(n-1) + fib(n-2)
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fib(6) =", fibonacci(6))  # 8

# 3. POWER FUNCTION
def power(base, exp):
    # Base cases
    if exp == 0:
        return 1
    if exp == 1:
        return base
    # Recursive: base^exp = base * base^(exp-1)
    return base * power(base, exp - 1)

print("2^5 =", power(2, 5))  # 32

# 4. SUM OF ARRAY
def sum_array(arr):
    # Base case
    if not arr:
        return 0
    # Recursive: arr[0] + sum(rest)
    return arr[0] + sum_array(arr[1:])

print("Sum [1,2,3,4,5] =", sum_array([1, 2, 3, 4, 5]))  # 15

# 5. REVERSE STRING
def reverse_string(s):
    # Base case
    if len(s) <= 1:
        return s
    # Recursive: last char + reverse(rest)
    return s[-1] + reverse_string(s[:-1])

print("Reverse 'hello':", reverse_string("hello"))  # "olleh"

# 6. PALINDROME CHECK
def is_palindrome_recursive(s):
    # Clean string
    s = ''.join(c.lower() for c in s if c.isalnum())
    
    # Base cases
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    # Recursive: check inner substring
    return is_palindrome_recursive(s[1:-1])

print("'racecar' palindrome:", is_palindrome_recursive("racecar"))  # True

# 7. BINARY SEARCH (recursive)
def binary_search_recursive(arr, target, left=0, right=None):
    if right is None:
        right = len(arr) - 1
    
    # Base case: not found
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    # Base case: found
    if arr[mid] == target:
        return mid
    # Recursive: search left or right half
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)

arr = [1, 3, 5, 7, 9, 11]
print("Index of 7:", binary_search_recursive(arr, 7))   # 3
print("Index of 4:", binary_search_recursive(arr, 4))   # -1

# 8. FIBONACCI WITH MEMOIZATION (optimization)
def fibonacci_memo(n, memo={}):
    if n in memo:
        return memo[n]
    
    if n <= 0:
        return 0
    if n == 1:
        return 1
    
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
    return memo[n]

print("Fib(40) optimized:", fibonacci_memo(40))  # 102334155 (fast)

# 9. PERMUTATIONS (generate all)
def permutations(s):
    # Base case
    if len(s) <= 1:
        return [s]
    
    result = []
    for i, char in enumerate(s):
        # Fix one character, permute the rest
        rest = s[:i] + s[i+1:]
        for perm in permutations(rest):
            result.append(char + perm)
    
    return result

print("Permutations of 'abc':", permutations("abc"))  
# ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

# 10. DIRECTORY TREE TRAVERSAL (real-world use)
import os

def list_files(path, indent=0):
    """Recursively list all files in directory tree"""
    try:
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            print("  " * indent + "├── " + item)
            
            # Recursive case: if directory, go deeper
            if os.path.isdir(full_path):
                list_files(full_path, indent + 1)
    except PermissionError:
        pass

# Uncomment to run (use with caution)
# list_files(".")

# WHEN TO USE RECURSION:
# - Tree/graph traversal (DFS, BFS)
# - Divide-and-conquer (merge sort, quick sort)
# - Backtracking (N-queens, maze solving)
# - Mathematical sequences (factorial, Fibonacci)
# - Problems with recursive structure (directory trees, XML/JSON)

# WARNING: 
# - Python has recursion limit (default ~1000)
# - Use sys.setrecursionlimit() to increase
# - Prefer iteration for deep recursion