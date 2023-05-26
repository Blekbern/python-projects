class Vertex:
    def __init__( self, id, name ):
        self . id               = id
        self . name             = name
        self . edges            = []            # std::vector<Edge> edges (EDGES LEADING OUT)
        self . minDistance      = float( 'inf' )
        self . previousVertex   = None          # Vertex previousVertex
        self . edgesIn          = []

class Edge:
    def __init__( self, source, target, weight ):
        self . source = source
        self . target = target
        self . weight = weight

class Dijkstra:
    def __init__( self ):
        self . vertexes     = [] # std::vector<Vertex> vertexes
        self . path         = {} #  "A": { "B": 2, "C": 3 }

    def setPath( self, edge ):
        if edge.source not in self.path.keys():
            self.path[edge.source] = {}
        self.path[edge.source][edge.target] = edge.weight


    def getVertex( self, id ):
        for vertex in self . vertexes:
            if vertex . id == id:
                return vertex


    def getMinVertex( self, queue ):
        min = None
        for vertex in queue:
            if min is None or vertex.minDistance < min.minDistance:
                min = vertex
        return min


    def computePath( self, sourceId ):
        currVertex = self.getVertex( sourceId )
        currVertex.minDistance = 0
        queue = []
        queue.append( currVertex )
        visited = []
        while queue:
            # Check if the current vertex has ANY paths leading OUT if NOT continue
            if currVertex.id not in self.path.keys():
                visited.append( currVertex )
                queue.remove( currVertex )
                currVertex = self.getMinVertex( queue )
                continue
            # Check every neighbor from the CURRENT VERTEX
            for neighbors in self.path[currVertex.id]:
                nxtVertex = self.getVertex( neighbors )
                # Skip iteration if the the next vertex IS already in VISITED
                if nxtVertex in visited:
                    continue
                # Check neighbor's current cost and compare with CURRENT VERTEX COST + pathCost TO NEXT VERTEX
                if currVertex.minDistance + self.path[currVertex.id][nxtVertex.id] < nxtVertex.minDistance:
                    nxtVertex.minDistance = currVertex.minDistance + self.path[currVertex.id][nxtVertex.id]
                    nxtVertex.previousVertex = currVertex
                # Make sure that the NEXT VERTEX is not already in the VISITED vertices
                if nxtVertex not in visited and nxtVertex not in queue:
                    queue.append( nxtVertex )
            visited.append( currVertex )        # mark curr vertex as visited
            queue.remove( currVertex )
            currVertex = self.getMinVertex( queue )


    def getShortestPathTo( self, targetId ):
        res = []
        currVertex = self.getVertex( targetId )
        while currVertex.previousVertex:
            res.append( currVertex )
            currVertex = currVertex.previousVertex
        res.append( currVertex )
        res.reverse()
        return res


    def createGraph( self, vertexes, edgesToVertexes ):
        self . vertexes = vertexes
        for vertices in vertexes:
            for edges in edgesToVertexes:
                if edges.source == vertices.id:
                    vertices.edges.append( edges )
                    self.setPath( edges )
                if edges.target == vertices.id:
                    vertices.edgesIn.append( edges )


    def resetDijkstra( self ):
        for vertices in self.vertexes:
            vertices . minDistance      = float( 'inf' )
            vertices . previousVertex   = None

    def getVertexes( self ):
        res = []
        for vertex in self.vertexes:
            if vertex.edges or vertex.edgesIn:
                res.append( vertex )
        return res

vertexes = [
  Vertex( 0, 'Redville'     ),  # 0
  Vertex( 1, 'Blueville'    ),  # 1
  Vertex( 2, 'Greenville'   ),  # 2
  Vertex( 3, 'Orangeville'  ),  # 3
  Vertex( 4, 'Purpleville'  ),  # 4
  Vertex( 5, 'Yellowvile'   ),  # 5
  Vertex( 6, 'Brownville'   )   # 6
]
edges = [
  Edge( 0, 1, 5  ),
  Edge( 0, 2, 10 ),
  Edge( 0, 3, 8  ),
  Edge( 1, 0, 5  ),
  Edge( 1, 2, 3  ),
  Edge( 1, 4, 7  ),
  Edge( 2, 0, 10 ),
  Edge( 2, 1, 3  ),
  Edge( 3, 0, 8  ),
  Edge( 3, 4, 2  ),
  Edge( 4, 1, 7  ),
  Edge( 4, 3, 2  ),
  Edge( 4, 6, 4  )
]
vertexes2 = [
Vertex( 0, 'Redvile'        ),
Vertex( 1, 'Blueville'      ),
Vertex( 2, 'Greenville'     ),
Vertex( 3, 'Orangeville'    ),
Vertex( 4, 'Purpleville'    ),
Vertex( 5, 'Someville'      )
]

edges2 = [
Edge( 0, 4, 23 ),
Edge( 0, 5, 58 ),
Edge( 0, 2, 88 ),
Edge( 0, 3, 48 ),
Edge( 1, 5, 99 ),
Edge( 1, 3, 76 ),
Edge( 1, 2, 58 ),
Edge( 1, 0, 59 ),
Edge( 1, 4, 14 ),
Edge( 2, 1, 64 ),
Edge( 2, 5, 90 ),
Edge( 2, 4, 19 ),
Edge( 3, 0, 99 ),
Edge( 4, 1, 76 ),
Edge( 4, 5, 64 ),
Edge( 4, 3, 36 ),
Edge( 5, 3, 7  ),
Edge( 5, 1, 94 )
]



dijkstra = Dijkstra()
dijkstra.createGraph(vertexes,edges)
dijkstraVertexes = dijkstra.getVertexes()
#Distance with path
for vertexToCompute in dijkstraVertexes:
    dijkstra.computePath(vertexToCompute.id)
    print('Printing min distance from vertex:'+str(vertexToCompute.name))
    #Print minDitance and path from current vertex to each other
    for vertex in dijkstraVertexes:
        print('Min distance to:'+str(vertex.name)+' is: '+str(vertex.minDistance))
        print('Path is:',end=" ")
        #Get shortest path to target vertex
        path = dijkstra.getShortestPathTo(vertex.id)
        for vertexInPath in path:
            print(str(vertexInPath.name),end=" ")
        print()
    print("-----------------------------------------------")
    #Reset Dijkstra between counting
    dijkstra.resetDijkstra()