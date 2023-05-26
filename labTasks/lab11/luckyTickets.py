# Calculates the probability of 'lucky' public ticket number occurence

# Tickets with a 6 digit serial number are considered 'lucky'

# when the sum of first and last 3 digits of the serial number are equal  


class LuckyNumberCounter:
  def __init__(self, digitCount):
    self.digitCount = digitCount
    self.numberCount = 1


  # as many methods as you need...


  def isLuckyNumber( self, number ):
    modifiedNum = str( number )
    sum1 = 0
    sum2 = 0
    isSudy = True
    # nejdriv si vypsat cisla o x digit-countu
    if isSudy:
        for i in range( int( len( modifiedNum ) / 2 ) ):
            sum1 += modifiedNum[i]
        for i in range( int( len( modifiedNum ), int( len( modifiedNum ) ) / 2, -1 ) ):
            sum2 += modifiedNum[i]
    if sum1 == sum2:
      return True

  def getLuckyNumberCount(self):
    return 1




luckyNum = LuckyNumberCounter( 6 )
luckyNum.isLuckyNumber( 531438 )

digits = 6
lnc = LuckyNumberCounter(digits)
luckyNumbersTotal = lnc.getLuckyNumberCount()
luckyNumbersProbab = luckyNumbersTotal / lnc.numberCount


print(lnc.digitCount, "digit lucky numbers count:", luckyNumbersTotal)
print("Probability of getting a lucky number is:", luckyNumbersProbab, end=" ")
print("so chance is 1 in", 1 / luckyNumbersProbab)
