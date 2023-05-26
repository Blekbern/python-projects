import random


secret = random.randint( 1, 100 )
guess = int( input( "Enter your guess:\n" ) )

if guess > 100 or guess < 1:
    raise ValueError( "Out of range!" )

while True:
    if guess == secret:
        print( "You win!" )
        break
    elif guess > secret:
        print( "Too large." )
    elif guess < secret:
        print( "Too small." )

print( "End of game" )