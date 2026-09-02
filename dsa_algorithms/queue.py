# Queue implementation using collections.deque (FIFO - First In First Out)

# deque (double-ended queue) - O(1) append/pop from BOTH ends
# list has O(1) append/pop from end, but O(n) for insert/pop from beginning
# Use deque when you need fast operations on both ends (queue, BFS, sliding window)
from collections import deque

# 1. CREATE an empty queue
queue = deque()
print("Empty queue:", queue)  # deque([])

# 2. ENQUEUE - add to the rear (right side) - O(1)
queue.append("Alice")   # queue: deque(['Alice'])
queue.append("Bob")     # queue: deque(['Alice', 'Bob'])
queue.append("Charlie") # queue: deque(['Alice', 'Bob', 'Charlie'])
print("After enqueues:", list(queue))  # ['Alice', 'Bob', 'Charlie']

# 3. DEQUEUE - remove from front (left side) - O(1)
served = queue.popleft()  # removes 'Alice'
print(f"Served: {served}")  # Output: Alice
print("After dequeue:", list(queue))  # ['Bob', 'Charlie']

# 4. PEEK - view front element without removing
if queue:
    front = queue[0]  # or queue[-1] for rear
    print("Next to serve:", front)  # Bob

# 5. CHECK if empty
print("Is queue empty?", len(queue) == 0)  # False

# 6. QUEUE with max size (bounded)
bounded = deque(maxlen=3)
bounded.append(1)
bounded.append(2)
bounded.append(3)
bounded.append(4)  # automatically removes 1 (oldest)
print("Bounded queue:", list(bounded))  # [2, 3, 4]

# 7. PROCESS all items (typical workflow)
while queue:
    customer = queue.popleft()
    print(f"Processing: {customer}")

# 8. ALTERNATIVE: list-based queue (inefficient - O(n) for pop(0))
# Not recommended - use deque instead

# Real-world uses: task scheduling, breadth-first search, print spooler, customer service lines