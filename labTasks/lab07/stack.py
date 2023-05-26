import dtb

class Stack:
    def __init__( self ):
        self . data = []

    def push( self, data ):
        self.data.append( data )

    def pop( self ):
        return None if self.is_empty() else self.data.pop()

    def size( self ):
        return len( self.data )

    def is_empty( self ):
        return self.size() == 0

    def print_items( self ):
        for i in self.data:
            print( i )


myStack = Stack()
myStack.push( dtb.Car( "BMW", 100000 ) )
myStack.push( dtb.Car( "VW", 77777 ) )
myStack.push( dtb.Car( "KIA", 900 ) )
myStack.push( dtb.Car( "Audi", 5000 ) )
myStack.print_items()
print( myStack.is_empty() )
print( "Popped:", myStack.pop() )
print( "Popped:", myStack.pop() )
print( "Popped:", myStack.pop() )
print( "Popped:", myStack.pop() )
print( myStack.is_empty() )
