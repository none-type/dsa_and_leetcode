# DFS (Depth-First Search) - explores as far as possible along each branch before backtracking
# O(V + E) time, O(V) space (call stack or explicit stack)

# 1. DFS ON GRAPH - RECURSIVE (most common)
def dfs_graph_recursive(graph, node, visited=None, order=None):
    if visited is None:
        visited = set()
        order = []
    
    visited.add(node)
    order.append(node)
    
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs_graph_recursive(graph, neighbor, visited, order)
    
    return order

# Example graph
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("DFS recursive from A:", dfs_graph_recursive(graph, 'A'))  # ['A', 'B', 'D', 'E', 'F', 'C']

# 2. DFS ON GRAPH - ITERATIVE (using stack)
def dfs_graph_iterative(graph, start):
    visited = set()
    stack = [start]
    order = []
    
    while stack:
        node = stack.pop()
        
        if node not in visited:
            visited.add(node)
            order.append(node)
            
            # Add neighbors (reverse order for consistent result)
            for neighbor in reversed(graph[node]):
                if neighbor not in visited:
                    stack.append(neighbor)
    
    return order

print("DFS iterative from A:", dfs_graph_iterative(graph, 'A'))  # ['A', 'C', 'F', 'E', 'B', 'D']

# 3. DFS ON BINARY TREE (3 traversals)
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

# Build tree:     1
#                / \
#               2   3
#              / \   \
#             4   5   6
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)

# Pre-order: Root -> Left -> Right
def dfs_preorder(node, result=None):
    if result is None:
        result = []
    if node:
        result.append(node.val)
        dfs_preorder(node.left, result)
        dfs_preorder(node.right, result)
    return result

print("Pre-order:", dfs_preorder(root))  # [1, 2, 4, 5, 3, 6]

# In-order: Left -> Root -> Right
def dfs_inorder(node, result=None):
    if result is None:
        result = []
    if node:
        dfs_inorder(node.left, result)
        result.append(node.val)
        dfs_inorder(node.right, result)
    return result

print("In-order:", dfs_inorder(root))   # [4, 2, 5, 1, 3, 6]

# Post-order: Left -> Right -> Root
def dfs_postorder(node, result=None):
    if result is None:
        result = []
    if node:
        dfs_postorder(node.left, result)
        dfs_postorder(node.right, result)
        result.append(node.val)
    return result

print("Post-order:", dfs_postorder(root))  # [4, 5, 2, 6, 3, 1]

# 4. FIND PATH BETWEEN NODES
def find_path(graph, start, target, path=None, visited=None):
    if path is None:
        path = [start]
        visited = set([start])
    
    if start == target:
        return path
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            visited.add(neighbor)
            result = find_path(graph, neighbor, target, path + [neighbor], visited)
            if result:
                return result
    
    return None

print("Path A to F:", find_path(graph, 'A', 'F'))  # ['A', 'B', 'E', 'F']

# 5. DETECT CYCLE IN GRAPH
def has_cycle(graph):
    visited = set()
    rec_stack = set()  # Tracks current recursion path
    
    def dfs(node):
        visited.add(node)
        rec_stack.add(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
            elif neighbor in rec_stack:
                return True
        
        rec_stack.remove(node)
        return False
    
    for node in graph:
        if node not in visited:
            if dfs(node):
                return True
    return False

print("Has cycle:", has_cycle(graph))  # True (B->D->B)

# 6. DFS ITERATIVE FOR TREE (with order control)
def dfs_tree_iterative(root, mode='pre'):
    if not root:
        return []
    
    result = []
    stack = [(root, False)]  # (node, processed)
    
    while stack:
        node, processed = stack.pop()
        
        if processed:
            result.append(node.val)
        else:
            if mode == 'pre':
                # Push right, left, then node (pre-order)
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
                stack.append((node, True))
            elif mode == 'in':
                # Push right, node, left (in-order)
                if node.right:
                    stack.append((node.right, False))
                stack.append((node, True))
                if node.left:
                    stack.append((node.left, False))
            else:  # post
                # Push node, right, left (post-order)
                stack.append((node, True))
                if node.right:
                    stack.append((node.right, False))
                if node.left:
                    stack.append((node.left, False))
    
    return result

print("Iterative pre-order:", dfs_tree_iterative(root, 'pre'))   # [1, 2, 4, 5, 3, 6]

# Real-world uses: maze solving, topological sorting, cycle detection, 
# file system traversal, web crawling, solving puzzles (sudoku, N-queens)