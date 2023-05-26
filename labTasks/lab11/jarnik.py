import queue

# slides - Jarnik example
graph1 = {
  "A": {"B": 2, "D": 6},
  "B": {"A": 2, "C": 3, "D": 8, "E": 5},
  "C": {"B": 3, "E": 7},
  "D": {"A": 6, "B": 8, "E": 9},
  "E": {"B": 5, "C": 7, "D": 9},
}

# whiteboard - Jarnik 2nd example
graph2 = {
  "A": {"B": 5, "F": 1},
  "B": {"A": 5, "C": 1, "D": 2, "E": 3, "G": 3},
  "C": {"B": 1},
  "D": {"B": 2, "E": 1, "G": 9},
  "E": {"B": 3, "D": 1, "F": 2},
  "F": {"A": 1, "E": 2},
  "G": {"B": 3, "D": 9}
}

# https://www.gatevidyalay.com/prims-algorithm-prim-algorithm-example/
# Problem 02

graph_g2 = {
  "A": {"B": 1, "C": 5},
  "B": {"A": 1, "C": 4, "D": 8, "E": 7},
  "C": {"A": 5, "B": 4, "D": 6, "F": 2},
  "D": {"B": 8, "C": 6, "E": 11, "F": 9},
  "E": {"B": 7, "D": 11, "F": 3, "G": 10},
  "F": {"C": 2, "D": 9, "E": 3, "G": 12},
  "G": {"E": 10, "F": 12}
}

# whiteboard - Jarnik vs Dijkstra example
graph3 = {
  "A": {"B": 6, "C": 10, "D": 8},
  "B": {"A": 6, "D": 3},
  "C": {"A": 10, "D": 5},
  "D": {"A": 8, "B": 3, "C": 5},
}

# slides - Dijktsra example
graph4 = {
  "A": {"B": 4, "C": 2},
  "B": {"A": 4, "C": 1, "D": 5},
  "C": {"A": 2, "B": 1, "D": 8, "E": 10},
  "D": {"B": 5, "C": 8, "E": 2, "F": 6},
  "E": {"C": 10, "D": 2, "F": 3},
  "F": {"D": 6, "E": 3},
}

pq = queue.PriorityQueue()
total_distance = 0
visited = []

act_vertex_id = "A"
act_distance = 0
prev_vertex_id = None

graph = graph1

pq.put( [act_distance, act_vertex_id, prev_vertex_id] )
while len( graph ) > len( visited ):
    while act_vertex_id in visited:        
        act_distance, act_vertex_id, prev_vertex_id = pq.get()
    print( f"Vertex {act_vertex_id}, distance: {act_distance} from: {prev_vertex_id}" )
    visited.append( act_vertex_id )
    total_distance += act_distance
    for vertex_id, distance in graph[act_vertex_id].items():
        pq.put( [distance, vertex_id, act_vertex_id] )
print( f"Total distance: {total_distance}" )

