def hello( n ):
    if n == 0:
        return
    print( "Hello" )
    hello( n - 1 )

hello( 5 )