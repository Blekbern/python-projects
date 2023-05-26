# ----------------------------- CLASSES -----------------------------

class Node:
    def __init__( self, value ):
        self . value    = value
        self . left     = None
        self . right    = None


class BinarySearchTree:
    def __init__( self ):
        self . root = None
        self . depth = 1
        

    def is_empty( self ):
        return self . root == None


    def insert( self, value ):
        newNode = Node( value )
        if self.is_empty():
            self.root = newNode
        else:
            curr_pos = self.root
            tmp = curr_pos                 # REMEMBER PREV POS TO LINK IT TOGETHER
            while curr_pos != None:        # FINDS LEAF AND GOES TO THE PLACE WHERE THE CHILD WOULD BE
                if value > curr_pos.value:
                    tmp = curr_pos
                    curr_pos = curr_pos.right
                else:
                    tmp = curr_pos
                    curr_pos = curr_pos.left
            if value < tmp.value:
                tmp.left = newNode
            else:
                tmp.right = newNode


    def fromArray( self, array ):
        for i in range( len( array ) ):
            newNode = Node( array[i] )
            if self.is_empty():
                self.root = newNode
            else:
                curr_pos = self.root
                tmp = curr_pos                 # REMEMBER PREV POS TO LINK IT TOGETHER
                while curr_pos != None:        # FINDS LEAF AND GOES TO THE PLACE WHERE THE CHILD WOULD BE
                    if array[i] > curr_pos.value:
                        tmp = curr_pos
                        curr_pos = curr_pos.right
                    else:
                        tmp = curr_pos
                        curr_pos = curr_pos.left
                if array[i] < tmp.value:
                    tmp.left = newNode
                else:
                    tmp.right = newNode


    def search( self, value ):
        self.depth = 1
        curr_pos = self.root
        while curr_pos:
            if curr_pos.value == value:
                return True
            elif value < curr_pos.value:
                self . depth += 1
                curr_pos = curr_pos.left
            elif value > curr_pos.value:
                self . depth += 1
                curr_pos = curr_pos.right
        self.depth -= 1 # WHEN NOT FOUND -> VISITED 'NONE' NODE (SUBTRACT THAT 1 NODE)
        return False


    def min( self ):
        if self.is_empty():
            return None
        tmp = self.root
        self.depth = 1
        while tmp.left:
            tmp = tmp.left
            self.depth += 1
        return tmp.value

    def max( self ):
        if self.is_empty():
            return None
        tmp = self.root
        self.depth = 1
        while tmp.right:
            tmp = tmp.right
            self.depth += 1
        return tmp.value

    def visitedNodes( self ):
        if self.is_empty():
            return None
        return self.depth
# ---------------------------- CLASSES ----------------------------


# ----------------------------- MAIN -----------------------------
# 
# binTree = BinarySearchTree()
# binTree.fromArray( [5, 3, 1, 4, 7, 6, 8] )
# 
# num_to_search = 12
# print( "SEARCHING FOR:", num_to_search, binTree.search( num_to_search ) )
# print( binTree.visitedNodes() )
# print( "--------------------" )
# 
# num_to_search = 4
# print( "SEARCHING FOR:", num_to_search, binTree.search( num_to_search )  )
# print( binTree.visitedNodes() )
# print( "--------------------" )
# 
# num_to_search = 3
# print( "SEARCHING FOR:", num_to_search, binTree.search( num_to_search ) )
# print( binTree.visitedNodes() )
# print( "--------------------" )
# 
# num_to_search = 5
# print( "SEARCHING FOR:", num_to_search, binTree.search( num_to_search )  )
# print( binTree.visitedNodes() )
# print( "--------------------" )
# 
# num_to_search = 32
# print( "SEARCHING FOR:", num_to_search, binTree.search( num_to_search ) )
# print( binTree.visitedNodes() )
# print( "--------------------" )
# 
# 
# 
# print( "MAX:", binTree.max() )
# print( binTree.visitedNodes() )
# print( "MIN:", binTree.min() )
# print( binTree.visitedNodes() )
# 
# binTree.insert( 12 )
# binTree.insert( 2 )
# binTree.insert( -4 )
# binTree.insert( 5 )
# 
# num_to_search = 5
# print( "SEARCHING FOR:", num_to_search, binTree.search( num_to_search ) )
# print( binTree.visitedNodes() )
# print( "--------------------" )
# 
# num_to_search = 2
# print( "SEARCHING FOR:", num_to_search, binTree.search( num_to_search ) )
# print( binTree.visitedNodes() )
# print( "--------------------" )
# 
# num_to_search = 4
# print( "SEARCHING FOR:", num_to_search, binTree.search( num_to_search ) )
# print( binTree.visitedNodes() )
# print( "--------------------" )
