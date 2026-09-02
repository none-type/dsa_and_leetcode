# BFS (Breadth-First Search) - explores level by level using a queue
# O(V + E) time, O(V) space

from collections import deque

# 1. BFS ON GRAPH (adjacency list)
def bfs_graph(graph, start):
    visited = set([start])
    queue = deque([start])
    order = []  # Track traversal order
    
    while queue:
        node = queue.popleft()
        order.append(node)
        
        # Explore all neighbors
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    
    return order

# Example graph (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("BFS from A:", bfs_graph(graph, 'A'))  # ['A', 'B', 'C', 'D', 'E', 'F']

# 2. BFS ON BINARY TREE (level-order traversal)
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def bfs_tree(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.val)
        
        # Add children to queue
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result

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

print("BFS tree:", bfs_tree(root))  # [1, 2, 3, 4, 5, 6]

# 3. SHORTEST PATH IN UNWEIGHTED GRAPH (BFS specialty)
def shortest_path(graph, start, target):
    visited = set([start])
    queue = deque([(start, [start])])  # (node, path)
    
    while queue:
        node, path = queue.popleft()
        
        if node == target:
            return path
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    
    return None  # No path

print("Shortest path A to F:", shortest_path(graph, 'A', 'F'))  # ['A', 'C', 'F']

# 4. LEVEL-BY-LEVEL (grouped by depth)
def bfs_levels(root):
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            level.append(node.val)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(level)
    
    return result

print("BFS levels:", bfs_levels(root))  # [[1], [2, 3], [4, 5, 6]]

# 5. FIND CONNECTED COMPONENTS
def connected_components(graph):
    visited = set()
    components = []
    
    for node in graph:
        if node not in visited:
            # BFS from this node
            component = []
            queue = deque([node])
            visited.add(node)
            
            while queue:
                curr = queue.popleft()
                component.append(curr)
                
                for neighbor in graph[curr]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            
            components.append(component)
    
    return components

print("Components:", connected_components(graph))  # [['A','B','C','D','E','F']]

# Real-world uses: shortest path, social network connections, web crawling, GPS navigation