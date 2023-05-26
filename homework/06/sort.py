
# ------------------------ my_sort ---------------------------
def insertSortAsc( data ):
    for i in range( len( data ) - 1 ):
        if data[i] < data[i + 1]:
            continue
        else:
            j = i
            while j >= 0 and data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                j -= 1
    tmp = data
    return data

def insertSortDesc( data ):
    for i in range( len( data ) - 1 ):
        if data[i] > data[i + 1]:
            continue
        else:
            j = i
            while j >= 0 and data[j] < data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                j -= 1
    tmp = data
    return data
# ------------------------------------------------------------



def sortNumbers(data, condition):
    if condition == "ASC":
        return insertSortAsc( data )        
    return insertSortDesc( data )


def sortData(weights, data, condition):
    if len( weights ) != len( data ):
        raise ValueError( 'Invalid input data' )
    tmp = list( zip( weights, data ) )
    if condition == "ASC":
        for i in range( len( tmp ) - 1 ):
            if tmp[i][0] < tmp[i + 1][0]:
                continue
            else:
                j = i
                while j >= 0 and tmp[j][0] > tmp[j + 1][0]:
                    tmp[j], tmp[j + 1] = tmp[j + 1], tmp[j]
                    j -= 1
    else:
        for i in range( len( tmp ) - 1 ):
            if tmp[i][0] > tmp[i + 1][0]:
                continue
            else:
                j = i
                while j >= 0 and tmp[j][0] < tmp[j + 1][0]:
                    tmp[j], tmp[j + 1] = tmp[j + 1], tmp[j]
                    j -= 1
    for i in range( len( tmp ) ):
        data[i] = tmp[i][1]
    tmp2 = data
    return tmp2
