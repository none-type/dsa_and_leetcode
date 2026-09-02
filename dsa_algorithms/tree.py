# Binary Tree - hierarchical structure with nodes (left/right children)

# 1. DEFINE NODE CLASS
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# 2. BUILD TREE
#        1
#       / \
#      2   3
#     / \
#    4   5
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

# 3. TRAVERSALS

# In-order (Left -> Root -> Right) - gives sorted order for BST
def inorder(node):
    if not node:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)
print("In-order:", inorder(root))  # [4, 2, 5, 1, 3]

# Pre-order (Root -> Left -> Right)
def preorder(node):
    if not node:
        return []
    return [node.val] + preorder(node.left) + preorder(node.right)
print("Pre-order:", preorder(root))  # [1, 2, 4, 5, 3]

# Post-order (Left -> Right -> Root)
def postorder(node):
    if not node:
        return []
    return postorder(node.left) + postorder(node.right) + [node.val]
print("Post-order:", postorder(root))  # [4, 5, 2, 3, 1]

# 4. BFS (Level-order) using queue
from collections import deque
def level_order(root):
    if not root:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result
print("Level-order:", level_order(root))  # [1, 2, 3, 4, 5]

# 5. SEARCH (find value)
def search(node, target):
    if not node:
        return False
    if node.val == target:
        return True
    return search(node.left, target) or search(node.right, target)
print("Find 5:", search(root, 5))  # True
print("Find 99:", search(root, 99))  # False

# 6. HEIGHT of tree
def height(node):
    if not node:
        return 0
    return 1 + max(height(node.left), height(node.right))
print("Tree height:", height(root))  # 3

# Real-world uses: file systems, HTML DOM, AI decision trees, expression parsing