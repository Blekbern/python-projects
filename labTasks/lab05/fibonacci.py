def fibo_list( n ):
    nums = [0, 1]
    if n == 0:
        return nums[0]
    if n == 0:
        return nums
    for i in range( n - 1 ):
        nums.append( nums[-1] + nums[-2] )
    return nums

print( fibo_list( 0 ) )
print( fibo_list( 1 ) )
print( fibo_list( 5 ) )
print( fibo_list( 10 ) )