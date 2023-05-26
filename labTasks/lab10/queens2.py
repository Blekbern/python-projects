class EightQueenPuzzle:

    def __init__(self, board_size: int):
        self . board_size   = board_size
        self . board        = [-1] * self.board_size

    def __str__(self) -> str:
        result = ""
        for r in self.board:
            for c in range(self.board_size):
                if r == c:
                    result += "X"
                else:
                    result += "_"
            result += "\n"
        return result

    def can_place( self, row: int, col: int ):
        for r in range(self.board_size):
            column: int = self.board[r]
            if col == column:
                return False
            # on primary or seconday diagonal:
            if column != -1 and abs(r - row) == abs(column - col):
                return False
        return True


    def place_queen( self, row ):
        if row == self.board_size:
            return
        for column in range( self.board_size ):
            if self.can_place( row, column ):
                self.board[row] = column     # puts queen
                if row == self.board_size - 1:
                    print( self )
                self.place_queen( row + 1 )
                self.board[row] = -1         # removes queen

eqp = EightQueenPuzzle(4)
eqp.place_queen(0)