def revert( lst ):
    if len( lst ) == 1:
        return lst
    n = lst.pop( 0 )
    return revert( lst ) + [n]

def revert2( lst ):
    if len( lst ) == 1:
        return lst
    return revert2( lst[1:] ) + lst[:1]



print( revert   ( [7, 8, 9, 10] ) )
print( revert2  ( [7, 8, 9, 10] ) )