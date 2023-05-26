myCars = [ "Ford", "Audi", "Alfa Romeo", "Skoda", "Toyota" ]


class CCars:
    
    def __init__( self, myList ):
        self.list = myList

#    ----------- BEFORE CLASS --------------
#    def print_items( myList ):
#        for i in range( len( myList ) ):
#            print( "Znacka: " + myList[i] )
#        # for i in myList:
#        #   print( "Znacka: ", i )

#    def contains_item( myList, item ):
#        for i in myList:
#            if item == i:
#                return True
#        return False

    def print_items( self ):
        for i in range( len( self.list ) ):
            print( "Znacka: " + self.list[i] )
        # for i in self.list:
        #   print( "Znacka: ", i )

    def contains_item( self, item ):
        for i in self.list:
            if item == i:
                return True
        return False

    def add_item( self, item ):
        if not self.contains_item( item ):
            self.list.append( item )

    def remove_item( self, item ):
        if self.contains_item( item ):
            self.list.remove( item )

    def revert_items( self ):
        # self.list.reverse()
        self.list = self.list[::-1] # dogshit reverse

# print_items( myCars )
# print( contains_item( myCars, "" ) )


carsList = CCars( myCars )
carsList.print_items()
print( carsList.contains_item( "Ford" ) )
print( carsList.contains_item( "baba" ) )
carsList.add_item( "BMW" )
carsList.print_items()
print( "================" )
carsList.remove_item( "BMW" )
carsList.print_items()
print( "================" )
carsList.revert_items()
carsList.print_items()