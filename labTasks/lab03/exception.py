while True:
    try:
        integer = int( input( "Enter integer:\n" ) )
    except ValueError:
        print( "Not an integer." )
    else:
        print( "All ok." )
        break