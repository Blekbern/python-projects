STATICKY_TEXT = "This is my static text which must be added to file. It is very long text and I do not know what they want to do with this terrible text. "
FILE_NAME = "output.txt"
def writeTextToFile( myPar ):
    with open( FILE_NAME, "w" ) as output:
        output.write( STATICKY_TEXT + str( myPar ) ) 
    return FILE_NAME