def polyEval(poly, x):
    polyRes = [ 0 ]
    j = 0
    for i in range( len( poly ) - 1, -1, -1 ):
        polyRes.append( x * polyRes[j] + poly[i] )
        j += 1
    return polyRes[j]

def polySum(poly1, poly2):
    if len( poly1 ) < len( poly2 ):
        polyRes = poly2
        for i in range( len( polyRes ) - len( poly1 ) ):
            poly1.append( 0 )
        for i in range( len( polyRes ) ):
            polyRes[i] = poly2[i] + poly1[i]
    else:
        polyRes = poly1
        for i in range( len( polyRes ) - len( poly2 ) ):
            poly2.append( 0 )
        for i in range( len( polyRes ) ):
            polyRes[i] = poly1[i] + poly2[i]
    while polyRes[i] == 0:
        polyRes.pop( i )
        i -= 1
    return polyRes

def polyMultiply(poly1, poly2):
    polyRes = []
    for i in range( len( poly1 ) + len( poly2 ) - 1 ):
        polyRes.append( 0 )
    for i in range( len( poly1 ) ):
        for j in range( len( poly2 ) ):
            polyRes[i + j] += poly1[i] * poly2[j]
    return polyRes


# print( polyEval( [-1, 2, -6, 2], 3 ) )
# print( polySum( [1, 2.5, 3.5, 0, 5.4], [-1, -3.5, -3.5, 0, -5.4] ) )
# print( polySum( [1, 2, 5], [2, 0, 1, -7] ) )
# print( polySum( [2, 0, 1, -7], [1, 2, 5] ) )
# print( polySum( [1, 1, 1, 2], [-1, -1, -1, -1] ))
# print( polyMultiply( [1, 2, 5], [2, 0, 1, -7] ) )