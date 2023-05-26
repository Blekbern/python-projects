import math


def newtonPi(init):
    res = init
    while abs( math.sin( res ) / math.cos( res ) ) >= 1e-15:
        res = res - ( math.sin( res ) / math.cos( res ) )
    return res


def leibnizPi( iterations ) :
    res = 0
    for i in range( iterations ):
        res += ( 4 * (-1)**(i) ) / (2 * i + 1)
    return res


def nilakanthaPi( iterations ) :
    res = 3
    for i in range( iterations - 1 ):
        res += (4 * (-1)**i) / ((2 * i + 3)**3 - (2 * i + 3))
    return res