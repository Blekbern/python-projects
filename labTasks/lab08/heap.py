class MaxHeap:
    def __init__( self, data ) -> None:
        self . data = data

    def get_left_child_i( self, index ):
        i = index * 2 + 1
        if i >= len( self.data ):
            return None
        return i
    
    def get_right_child_i( self, index ):
        i = index * 2 + 2
        if i >= len( self.data ):
            return None
        return i
    
    def sift_down( self, index ):
        li = self.get_left_child_i( index )
        ri = self.get_right_child_i( index )
        tmp_max_index = index
        if li != None and self.data[li] > self.data[tmp_max_index]:
            tmp_max_index = li
        if ri != None and self.data[ri] > self.data[tmp_max_index]:
            tmp_max_index = ri
        if tmp_max_index != index:
            self.data[tmp_max_index], self.data[index] = self.data[index], self.data[tmp_max_index]
            self.sift_down( tmp_max_index )

    def heapify( self ):
        last_index = len( self.data ) - 1
        last_with_child = (last_index - 1) // 2 # TODO: check!
        for i in range( len( self.data ) - 1, -1, -1 ):
            self . sift_down( i )

mh = MaxHeap( [15, 19, 10, 7, 17, 16] )
# print( mh.get_left_child_i( 2 ) )
# print( mh.get_right_child_i( 2 ) )
print( mh.data )
# mh.sift_down( 0 )
# print( mh.data )

mh.heapify()
print( mh.data )