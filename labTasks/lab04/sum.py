def sum_num( num_min, num_max ):
    res = 0
    for i in range( num_min, num_max + 1 ):
        res += i
    return res

print( sum_num( 5, 10 ) )

def sumWhile( num_min, num_max ):
    res = 0
    i = num_min
    while i < num_max + 1:
        res += i
        i += 1
    return res

print( sumWhile( 5, 10 ) )
