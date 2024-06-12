import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, visited_nodes_colors=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    if visited_nodes_colors:
        for node_id, color in visited_nodes_colors.items():
            tree.nodes[node_id]['color'] = color

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def build_heap_tree(heap):
    if not heap:
        return None
    
    nodes = [Node(key) for key in heap]
    for i in range(len(nodes)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(nodes):
            nodes[i].left = nodes[left_index]
        if right_index < len(nodes):
            nodes[i].right = nodes[right_index]
    return nodes[0]

def get_color_gradient(n):
    colors = []
    for i in range(n):
        ratio = i / (n - 1) if n > 1 else 1
        hex_color = "#{:02x}{:02x}{:02x}".format(int(18 + 218 * ratio), int(150 + 100 * ratio), int(240 * ratio))
        colors.append(hex_color)
    return colors

def dfs(tree_root):
    visited_nodes = []
    stack = [tree_root]
    while stack:
        node = stack.pop()
        if node:
            visited_nodes.append(node)
            stack.append(node.right)
            stack.append(node.left)
    return visited_nodes

def bfs(tree_root):
    visited_nodes = []
    queue = deque([tree_root])
    while queue:
        node = queue.popleft()
        if node:
            visited_nodes.append(node)
            queue.append(node.left)
            queue.append(node.right)
    return visited_nodes

def visualize_traversal(tree_root, traversal_func):
    visited_nodes = traversal_func(tree_root)
    colors = get_color_gradient(len(visited_nodes))
    visited_nodes_colors = {node.id: colors[i] for i, node in enumerate(visited_nodes)}
    draw_tree(tree_root, visited_nodes_colors)

# Приклад купи
heap = [10, 7, 5, 3, 2, 4, 1, 12, 15, 112, 1, 23, 55, 61, 15, 22, 33, 44, 56, 90, 1341]

# Побудова дерева
heap_tree_root = build_heap_tree(heap)

# Обхід в глибину
print("DFS Traversal:")
visualize_traversal(heap_tree_root, dfs)

# Обхід в ширину
print("BFS Traversal:")
visualize_traversal(heap_tree_root, bfs)
