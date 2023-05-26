class Car:
    def __init__( self, brand: str, price: int ) -> None:
        self . brand = brand
        self . price = price

    def __str__( self ):
        return f"Car brand: {self.brand}, price: {self.price}"


myCar = Car( "BMW", 100000 )
# print( myCar )