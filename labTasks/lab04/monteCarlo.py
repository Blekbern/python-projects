import random, math

def get_pi( cnt: int ) -> float:
    in_circle: int = 0
    for i in range( cnt ):
        x: float = random.uniform( -1, 1 )
        y: float = random.uniform( -1, 1 )
        d: float = math.sqrt( x**2 + y**2 )
        if d <= 1:
            in_circle += 1
    return 4 * ( in_circle / cnt )


print( get_pi( 500000 ) )