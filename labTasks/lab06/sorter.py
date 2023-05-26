import random

class data_sorter:
    def __init__( self, item_cnt: int, from_num: int, to_num: int ) -> None:
        self.data: list(int) = []
        for i in range(item_cnt):
            self.data.append( random.randint( from_num, to_num ) )

    def __str__( self ) -> None:
        result: str = ""
        for item in self.data:
            result += str( item ) + " "
        return result

    def swap_num( self, x: int, y: int ) -> None:
        self.data[x], self.data[y] = self.data[y], self.data[x]

    def max( self ) -> int:
        max = self.data[0]
        for i in range( 1, len(self.data) ):
            if self.data[i] > max:
                max = self.data[i]
        return max

    def bubble_sort( self ) -> None:
        for j in range( len( self.data ) ):
            was_swap = False
            for i in range( len( self.data) - 1 - j ):
                if self.data[i] > self.data[i + 1]:
                    self.swap_num( i, i + 1 )
                    was_swap = True
            if not was_swap:
                break

    # DODELAT
    def selection_sort( self ) -> None:
        min_num_index = 0
        for i in range( min_num_index, len( self.data ) ):
            if self.data[i] < self.data[min_num_index]:
                min_num_index = i
        self.swap( )
    # DODELAT        


sorter = data_sorter( 10, 1, 1000 )
print( sorter )
sorter.swap_num( 2, 7 )
print( sorter )
print( sorter.max() )
sorter.bubble_sort()
print( sorter )