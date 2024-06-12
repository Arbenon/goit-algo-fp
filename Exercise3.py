import heapq

class Graph:
    def __init__(self):
        self.edges = {}

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex not in self.edges:
            self.edges[from_vertex] = []
        if to_vertex not in self.edges:
            self.edges[to_vertex] = []
        self.edges[from_vertex].append((to_vertex, weight))
        # Якщо граф не орієнтований, додайте також зворотне ребро
        # self.edges[to_vertex].append((from_vertex, weight))

def dijkstra(graph, start_vertex):
    min_heap = []
    heapq.heappush(min_heap, (0, start_vertex))
    distances = {vertex: float('infinity') for vertex in graph.edges}
    distances[start_vertex] = 0
    visited = set()

    while min_heap:
        current_distance, current_vertex = heapq.heappop(min_heap)
        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph.edges.get(current_vertex, []):
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(min_heap, (distance, neighbor))

    return distances

# Приклад використання
graph = Graph()
graph.add_edge('A', 'B', 1)
graph.add_edge('A', 'C', 4)
graph.add_edge('A', 'E', 7)
graph.add_edge('B', 'C', 2)
graph.add_edge('B', 'D', 5)
graph.add_edge('C', 'D', 1)
graph.add_edge('C', 'E', 3)
graph.add_edge('D', 'E', 1)
graph.add_edge('D', 'F', 6)
graph.add_edge('E', 'F', 2)
graph.add_edge('E', 'G', 8)
graph.add_edge('F', 'G', 3)

start_vertex = 'A'
distances = dijkstra(graph, start_vertex)

print(f"Найкоротші відстані від вершини {start_vertex}:")
for vertex, distance in distances.items():
    print(f"Відстань до вершини {vertex}: {distance}")

