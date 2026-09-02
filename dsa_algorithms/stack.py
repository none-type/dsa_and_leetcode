# Stack implementation using Python list (LIFO - Last In First Out)

# Create an empty stack
stack = []

# PUSH - add elements to the top
stack.append(10)  # stack: [10]
stack.append(20)  # stack: [10, 20]
stack.append(30)  # stack: [10, 20, 30]
print("After pushes:", stack)

# POP - remove and return the top element
top = stack.pop()  # removes 30
print("Popped:", top)        # Output: 30
print("After pop:", stack)   # Output: [10, 20]

# PEEK - view top element without removing
if stack:
    print("Top element:", stack[-1])  # Output: 20

# CHECK if empty
print("Is stack empty?", len(stack) == 0)  # Output: False

# Real-world use: Undo functionality, expression evaluation, backtracking