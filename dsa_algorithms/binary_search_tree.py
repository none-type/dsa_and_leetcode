# BST (Binary Search Tree) - left < root < right, O(log n) average operations

class BSTNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 1. INSERT - O(log n) average
def insert(root, val):
    if not root:
        return BSTNode(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

# Build BST: insert 5, 3, 7, 1, 4, 6, 8
root = None
for v in [5, 3, 7, 1, 4, 6, 8]:
    root = insert(root, v)
# Tree:
#       5
#      / \
#     3   7
#    / \ / \
#   1  4 6  8

# 2. SEARCH - O(log n) average
def search(root, target):
    if not root or root.val == target:
        return root
    if target < root.val:
        return search(root.left, target)
    return search(root.right, target)
print("Find 4:", search(root, 4) is not None)  # True

# 3. FIND MIN/MAX
def find_min(root):
    while root.left:
        root = root.left
    return root.val
print("Min:", find_min(root))  # 1

# 4. DELETE - O(log n) average
def delete(root, val):
    if not root:
        return None
    if val < root.val:
        root.left = delete(root.left, val)
    elif val > root.val:
        root.right = delete(root.right, val)
    else:
        # Case 1: leaf or one child
        if not root.left:
            return root.right
        if not root.right:
            return root.left
        # Case 2: two children - replace with inorder successor (min of right)
        root.val = find_min(root.right)
        root.right = delete(root.right, root.val)
    return root

# Delete 3 (has two children)
root = delete(root, 3)

# 5. IN-ORDER traversal - gives sorted order! O(n)
def inorder(root):
    if not root:
        return []
    return inorder(root.left) + [root.val] + inorder(root.right)
print("Sorted order:", inorder(root))  # [1, 4, 5, 6, 7, 8]

# 6. VALIDATE BST
def is_valid(root, low=float('-inf'), high=float('inf')):
    if not root:
        return True
    if not (low < root.val < high):
        return False
    return (is_valid(root.left, low, root.val) and 
            is_valid(root.right, root.val, high))
print("Is valid BST:", is_valid(root))  # True

# Real-world uses: database indexing, autocomplete, sorted data storage