"""
Homer's fridge
Course: B0B36ZAL
"""

#nasledujici kod nijak nemodifikujte!
class Food:
    def __init__(self, name, expiration):
        self.name = name
        self.expiration = expiration
#predesly kod nijak nemodifikujte!

def openFridge(fridge):
    print("Following items are in Homer's fridge:")
    for food in fridge:
        print("{0} (expires in: {1} days)".format(
            str(food.name), str(food.expiration))
        )
    print("")

"""
Task #1
"""
def maxExpirationDay( fridge ): # std::vector< Food > fridge
    if not fridge:
        return -1
    # Take the first item as the max
    maxExp = fridge[0].expiration
    for item in fridge:
        if item.expiration > maxExp:
            maxExp = item.expiration
    return maxExp

"""
Task #2
"""
def histogramOfExpirations( fridge ):
    res = []
    for i in range( maxExpirationDay( fridge ) + 1 ):
        cnt = 0
        for item in fridge:
            if item.expiration == i:
                cnt += 1
        res.append( cnt )
    return res

"""
Task #3
"""
def cumulativeSum( histogram ):    
    res = []
    if not histogram:
        return res
    res.append( histogram[0] )
    for i in range( 1, len( histogram ) ):
        res.append( histogram[i] + res[i - 1] )
    return res

"""
Task #4
"""
def sortFoodInFridge( fridge ):
    tmp = cumulativeSum( histogramOfExpirations( fridge ) )
    res = len( fridge ) * [None]
    for item in fridge:
        exp = item.expiration
        tmp[exp] -= 1
        posInd = tmp[exp]
        res[posInd] = item
    return res

"""
Task #5
"""
def reverseFridge(fridge):
    res = fridge[::-1]
    return res

"""
Task #6
"""
def eatFood(name, fridge):
    tmp = fridge[:]
    contains_food = False
    index = 0
    min = float( 'inf' )
    for item in tmp:
        if item.name == name:
            contains_food = True
            if item.expiration < min:
                index = tmp.index( item )
                min = item.expiration
    if contains_food:
        tmp.pop( index )
    return tmp
