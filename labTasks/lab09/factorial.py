def factorial( n ):
    if n == 0:
        return 1
    else:
        return n * factorial( n - 1 )

def fact_iter( n ):
    res = 1
    for i in range( 1, n + 1 ):
        res *= i
    return res

print( factorial( 0 ) )
print( factorial( 2 ) )
print( factorial( 1 ) )
print( factorial( 3 ) )
print( factorial( 4 ) )
print( factorial( 5 ) )
print( factorial( 6 ) )