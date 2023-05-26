def sqrt_a( a ):
    x = a
    while True:
        xn = (x + a / x ) / 2
        if xn == x:
            return x
        x = xn
        
print( sqrt_a( 9 ) )