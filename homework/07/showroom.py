
# ------------------------------ CLASSES -------------------------------

class Car:
    def __init__( self, identification: int, name: str, brand: str, price: int, active: bool ):
        self . identification    = identification
        self . name              = name
        self . brand             = brand
        self . price             = price
        self . active            = active

class Node:
    def __init__( self, nextNode, prevNode, data: Car ):
        self . data     = data
        self . nextNode = nextNode
        self . prevNode = prevNode


class LinkedList:
    def __init__( self ):
        self . head = None
        self . tail = None

# ----------------------------------------------------------------------

db = LinkedList()

# ------------------------------ FUNCTIONS ------------------------------

def init( cars ): # cars = [ CCar car1, CCar car2, CCar car3, CCar car4 ]
    cars.sort( key = lambda x: x.price )
    db.head = db.tail = Node( None, None, cars[0] )
    for i in range(1, len(cars) ):
        db.tail.nextNode = Node( None, db.tail, cars[i] )
        db.tail = db.tail.nextNode


def add( car ):
    #if empty
    if db.head == db.tail == None:
        db.head = db.tail = Node( None, None, car )

    # for the lowest price
    elif car.price < db.head.data.price:
        newNode = Node( db.head, None, car )
        db.head = newNode
        db.head.nextNode.prevNode = newNode

    # for the highest price
    elif car.price > db.tail.data.price:
        newNode = Node( None, db.tail, car )
        db.tail = newNode
        db.tail.prevNode.nextNode = newNode
    
    # in the middle    
    else:
        curr_pos = db.tail.prevNode
        while car.price < curr_pos.data.price:
            curr_pos = curr_pos.prevNode
        newNode = Node( curr_pos.nextNode, curr_pos.prevNode, car )
        curr_pos.nextNode = newNode
        curr_pos.nextNode.prevNode = curr_pos
        newNode.nextNode.prevNode = newNode

def updateName( identification, name ):
    curr_pos = db.head
    while curr_pos:
        if curr_pos . data . identification == identification:
            curr_pos. data . name = name
            return True
        else:
            curr_pos = curr_pos.nextNode
    return None # car ID not found


def updateBrand( identification, brand ):
    curr_pos = db.head
    while curr_pos:
        if curr_pos . data . identification == identification:
            curr_pos. data . brand = brand
            return True
        else:
            curr_pos = curr_pos.nextNode
    return None # car ID not found


def activateCar( identification ):
    curr_pos = db.head
    while curr_pos:
        if curr_pos.data.identification == identification:
            curr_pos.data.active = True
            return True
        else:
            curr_pos = curr_pos.nextNode
    return None # car ID not found

def deactivateCar( identification ):
    curr_pos = db.head
    while curr_pos:
        if curr_pos.data.identification == identification:
            curr_pos.data.active = False
            return True
        else:
            curr_pos = curr_pos.nextNode
    return None # car ID not found
    

def getDatabaseHead():
    return db.head


def getDatabase():
    return db


def calculateCarPrice():
    curr_pos = db.head
    sum = 0
    while curr_pos:
        if curr_pos.data.active == True:
            sum += curr_pos.data.price
        curr_pos = curr_pos.nextNode
    return sum

def clean():
    db . head = None
    db . tail = None

# ------------------------------ FUNCTIONS ------------------------------


# -------------------------------- MAIN ---------------------------------
# ----- DEBUGGING:
# car1 = Car( 1, "Pepa",  "BMW",      10000,  True    )
# car2 = Car( 2, "Honza", "Ford",     5500,   True    )
# car3 = Car( 3, "Josef", "BMW",      7777,   True    )
# car4 = Car( 4, "Pepa",  "Toyota",   3000,   False   )
# car5 = Car( 5, "Jirka", "Mercedes", 49999,  False   )
# cars = [car1, car2, car3, car4, car5]
# 
# for i in range( len( cars ) ):
#     print( cars[i].identification )
# 
# # 4, 2, 3, 1, 5
# init( cars )
# LINKED LIST INITIALIZED AND SORTED
# 
# print( "---------------" )
# 
# 
# for i in range( len( cars ) ):
#     print( cars[i].identification )
# 
# 
# print( "---------------" )
# 
# 
# for i in range( len(cars) ):
#     if cars[i].identification == 3:
#         print( cars[i].name )
#         break
# updateName( 3, "Pepa" ) # RENAMING CAR WITH ID 3
# for i in range( len(cars) ):
#     if cars[i].identification == 3:
#         print( cars[i].name )
#         break
# 
# 
# print( updateName( 10, "Pepa" ) ) # LOOKING FOR CAR WITH ID 10 -> NOT FOUND (NONE)
# 
# 
# print( "---------------" )
# 
# 
# add( car1 )
# add( Car( 6, "Laura",   "Nissan",   10,          False ) )
# add( Car( 7, "Daniel",  "Honda",    4,          False ) )
# add( Car( 8, "Adam",    "Citroen",  12,      False ) )
# add( Car( 9, "Ondra",   "Opel",     999999,     True ) )
# 
# 
# curr_pos = db.head
# while curr_pos:
#     print(  curr_pos.data.identification, curr_pos.data.name, curr_pos.data.brand, curr_pos.data.price, curr_pos.data.active )
#     print( curr_pos.prevNode )
#     print( curr_pos )
#     print( curr_pos.nextNode )
#     print( "---------------" )
#     curr_pos = curr_pos.nextNode
# 
# print( "---------------" )
# 
# 
# print( activateCar( 4 ) )
# print( activateCar( 10 ) )
# 
# print( "---------------" )
# 
# 
# print( calculateCarPrice() )
# 
# 
# print( "---------------" )
# 
# 
# 
# print( getDatabase() )
# print( getDatabaseHead() )