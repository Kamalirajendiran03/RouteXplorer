This repository contains a Python-based Location-Based Route Planner application that utilizes the A* algorithm to find the shortest path between different locations.
The project aims to provide users with a convenient tool for planning optimal routes based on their input of locations and connections.

Features:
Graph Representation: Locations are represented as vertices, and connections between them are represented as edges in a graph data structure.

A Algorithm:* The A* algorithm efficiently computes the shortest path between two locations by considering both the actual cost from the start point and a heuristic estimate of the cost to the destination.

User Input Interface: The application prompts users to input location names, connections, and distances between them, offering flexibility in defining the map and customizing routes.

Shortest Path Visualization: Once the shortest path is computed, the application displays the route, highlighting each location in the order it should be visited for easy navigation.

Error Handling: The application gracefully handles invalid inputs, providing informative messages if no valid route exists between specified locations or if input data is incorrect.

