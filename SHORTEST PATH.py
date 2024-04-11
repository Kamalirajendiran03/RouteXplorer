import heapq

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        self.adjacency_list[vertex] = {}

    def add_edge(self, vertex1, vertex2, weight):
        self.adjacency_list[vertex1][vertex2] = weight
        self.adjacency_list[vertex2][vertex1] = weight

    def get_neighbors(self, vertex):
        return self.adjacency_list[vertex]

    def heuristic(self, vertex1, vertex2):
        # Placeholder heuristic function
        return 0

    def a_star(self, start_vertex, end_vertex):
        distances = {vertex: float('inf') for vertex in self.adjacency_list}
        distances[start_vertex] = 0

        priority_queue = [(0, start_vertex)]

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            if current_distance > distances[current_vertex]:
                continue

            if current_vertex == end_vertex:
                break

            for neighbor, weight in self.get_neighbors(current_vertex).items():
                distance = distances[current_vertex] + weight
                heuristic = self.heuristic(neighbor, end_vertex)
                total_distance = distance + heuristic

                if total_distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (total_distance, neighbor))

        return distances

def route_planner(graph, start_location, end_location):
    distances = graph.a_star(start_location, end_location)
    shortest_distance = distances[end_location]

    if shortest_distance == float('inf'):
        return "There is no valid route between the locations."

    # Backtrack to find the shortest path
    path = []
    current_location = end_location
    while current_location != start_location:
        path.append(current_location)
        neighbors = graph.get_neighbors(current_location)
        current_location = min(neighbors, key=lambda x: distances[x])

    path.append(start_location)
    path.reverse()

    return path

# Create a graph representing the locations
location_graph = Graph()

# Get user input for the number of locations
num_locations = int(input("Enter the number of locations: "))

# Get user input for the locations and their connections
for _ in range(num_locations):
    location = input("Enter the location name: ")
    location_graph.add_vertex(location)

num_connections = int(input("Enter the number of connections between locations: "))

for _ in range(num_connections):
    connection = input("Enter a connection (e.g., Location1 Location2 Distance): ").split()
    location1, location2, distance = connection[0], connection[1], float(connection[2])
    location_graph.add_edge(location1, location2, distance)

# Get user input for the start and end locations
start_location = input("Enter the start location: ")
end_location = input("Enter the end location: ")

# Find the shortest path between the start and end locations
path = route_planner(location_graph, start_location, end_location)
print("Shortest path:", path)

# Traverse the shortest path
print("Traversal of the shortest path:")
for location in path:
    print(location)
