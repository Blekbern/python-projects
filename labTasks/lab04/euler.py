def factorial( n ):
    res = 1
    for i in range( 1, n + 1 ):
        res *= i
    return res

def euler( n ):
    res = 0
    for i in range(n):
        res += 1 / factorial( i )
    return res

print( euler( 2 ) ) # 1 + 1