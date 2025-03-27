import heapq

#implementing Romania Map as Priority Queue
romaniaMap = {
    'Arad': [('Sibiu',140), ('Zerind',75), ('Timisoara',118)],
    'Zerind': [('Oradea',71)],
    'Oradea': [('Sibiu',151)],
    'Sibiu': [('Fagaras',99), ('Rimnicu',80)],
    'Timisoara': [('Lugoj',111)],
    'Lugoj': [ ('Mehadia',70)],
    'Mehadia': [ ('Drobeta',75)],
    'Drobeta': [('Craiova',120)],
    'Craiova': [('Rimnicu',146), ('Pitesti',138)],
    'Rimnicu': [( 'Pitesti',97)],
    'Fagaras': [( 'Bucharest',211)],
    'Pitesti': [( 'Bucharest',101)],
    'Bucharest': [ ('Giurgiu',90), ('Urziceni',85)],
    'Giurgiu': [],
    'Urziceni': [( 'Vaslui',142), ('Hirsova',98)],
    'Hirsova': [( 'Eforie',86)],
    'Eforie': [],
    'Vaslui': [('Iasi',92)],
    'Iasi': [( 'Neamt',87)],
    'Neamt': []
}

def uniform_cost_search(graph, start, goal):
    # Priority queue to store the frontier nodes, initialized with the start node
    priority_queue = [(0, start)]
    # Dictionary to store the cost of the shortest path to each node
    visited = {start: (0, None)}
    
    while priority_queue:
        # Pop the node with the lowest cost from the priority queue
        current_cost, current_node = heapq.heappop(priority_queue)
        
        # If we reached the goal, return the total cost and the path
        if current_node == goal:
            return current_cost, reconstruct_path(visited, start, goal)
        
        # Explore the neighbors
        for neighbor, cost in graph[current_node]:
            total_cost = current_cost + cost
            # Check if this path to the neighbor is better than any previously found
            if neighbor not in visited or total_cost < visited[neighbor][0]:
                visited[neighbor] = (total_cost, current_node)
                heapq.heappush(priority_queue, (total_cost, neighbor))
    
    # If the goal is not reachable, return None
    return None

def reconstruct_path(visited, start, goal):
    # Reconstruct the path from start to goal by following the visited nodes
    path = []
    current = goal
    while current is not None:
        path.append(current)
        current = visited[current][1]  # Get the parent node
    path.reverse()
    return path



# Example usage of the UCS function
start_node = 'Arad'
goal_node = 'Bucharest'
result = uniform_cost_search(romaniaMap, start_node, goal_node)

if result:
    total_cost, path = result
    print(f"Least cost path from {start_node} to {goal_node}: {' -> '.join(path)} with total cost {total_cost}")
else:
    print(f"No path found from {start_node} to {goal_node}")
