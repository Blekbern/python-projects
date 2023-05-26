sum = 0
cnt = 0
while True:
    mark = int( input( "Zadej znamku:\n" ) )
    if mark == 0:
        break
    sum += mark
    cnt += 1
    
print( sum / cnt )