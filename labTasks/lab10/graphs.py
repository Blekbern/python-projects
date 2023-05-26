class graphTraverser:
    def __init__( self, graph ):
        self . graph    = graph
        self . visited  = []

    def dfs_tree( self, vertex ):
        print( vertex )
        for neighbor in self.graph[vertex]:
            self.dfs_tree( neighbor )

    def dfs( self, vertex ):
        self.visited = []
        self.dfs_internal( vertex )

    def dfs_internal( self, vertex ):
        print( vertex )
        self.visited.append( vertex )
        for neighbor in self.graph[vertex]:
            if neighbor not in self.visited:
                self.dfs_internal( neighbor )

    def dfs_iter( self, vertex ):
        self.visited = []
        stack = [vertex]
        while True:
            while vertex in self.visited:
                if stack:
                    vertex = stack.pop(0)
                else:
                    return
            print( vertex )
            self.visited.append( vertex )
            stack = self.graph[vertex] + stack

    def bfs( self, vertex ):
        self.visited = []
        queue = [vertex]
        while True:
            while vertex in self.visited:
                if queue:
                    vertex = queue.pop(0)
                else:
                    return
            print( vertex )
            self.visited.append( vertex )
            queue = queue + self.graph[vertex]





tree = {
  "A": ["B", "C"],
  "B": ["D", "E"],
  "D": [],
  "E": [],
  "C": []
}


g1 = {
  "A": ["B", "C"],
  "B": ["D", "E"],
  "D": ["E"],
  "E": ["A"],
  "C": ["D", "E"]
}

graph1 = {
  "A": ["B", "D"],
  "B": ["C", "F"],
  "C": ["E", "G", "H"],
  "G": ["E", "H"],
  "E": ["B", "F"],
  "F": ["A"],
  "D": ["F"],
  "H": ["A"]
}


gt = graphTraverser( graph1 )
gt.bfs( "A" )
