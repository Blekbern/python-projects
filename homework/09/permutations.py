def permutations( array ):
    if len( array ) == 0 or len( array ) == 1:
        return [array]
    res = []
    for i in range( len( array ) ):
        array[0], array[i] = array[i], array[0]
        remainders = permutations( array[1:] )  #  [ P[remainders] ]
        for j in range( len( remainders ) ):    #  [1, 2, 3]
            res += [[array[0]] + remainders[j]] #  1 + P[2, 3]
    return res

# print( permutations( [1, 2, 3] ) )
# print( "-------------------" )
# print( permutations( [1, 2, 3, 4] ) )
# print( "-------------------" )
# print( permutations( ['a', 'b', 'c'] ) )
# print( "-------------------" )
# print( permutations( ['a', 'b', 'c', 'd'] ) )
# print( "-------------------" )
# print( permutations( [] ) )
# print( "-------------------" )
# print( permutations( [1] ) )
# print( permutations( [1, 'a', 2] ) )








