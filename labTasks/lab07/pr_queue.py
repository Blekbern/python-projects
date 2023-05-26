import dtb

class Stack:
    def __init__( self ):
        self . data = []

    def push( self, item ):
        if self.is_empty():
            self.data.append( item )
            return
        for i in range( len( self.data ) ):
            if item.price > self.data[i].price:
                self.data.insert( i, item )
                return
        self.data.append( item )
        
    def pop( self ):
        return None if self.is_empty() else self.data.pop( 0 )

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
