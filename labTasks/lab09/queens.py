
size = 4

def can_place( row, col ):
    return True # TODO

def winner():
    pass # TODO

def place_queen( row ):
    for i in range( size ):
        if can_place( row, col ):
            board[row] = column # puts queen
            if row == size - 1:
                winner()
            place_queen( row + 1 )
            board[row] = -1 # removes queen
