import random

class Dealer:
  def __init__(self):
    self . deck = [
      '♥A', '♥7', '♥8', '♥9', '♥10', '♥J', '♥Q', '♥K',
      '♦A', '♦7', '♦8', '♦9', '♦10', '♦J', '♦Q', '♦K',
      '♣A', '♣7', '♣8', '♣9', '♣10', '♣J', '♣Q', '♣K',
      '♠A', '♠7', '♠8', '♠9', '♠10', '♠J', '♠Q', '♠K'
    ]
    self . players = []

  def shuffle( self ):
    tmp = []
    upper_bound = len( self.deck ) - 1
    while self.deck:
      i = random.randint( 0, upper_bound )
      tmp.append( self.deck[i] )
      self.deck.remove( self.deck[i] )
      upper_bound -= 1
    self.deck = tmp

  def deal( self, n ):
    res = []
    for i in range( n ):
      if not self.deck:
        return res
      res.append( self.deck[i] )
      self.deck.remove( self.deck[i] )
    return res

  def addPlayer(self, player):
    self.players.append( player )

  def removePlayer(self, player):
    self.players.remove( player )

  def startRound(self):
    stop_cnt = 0
    for i in range( len( self.players ) ):
      self.players[i].hand.append( self.deal( 1 ) )
    while stop_cnt != len( self.players ):
      for i in range( len( self.players ) ):
        if self.players[i].needsCard():
          self.players[i].acceptCard( self.deal( 1 ) )
    self.announceWinner()
        
  def announceWinner(self):
    return
    

class Player:
  def __init__(self, name, strategy):
    self . name     = name
    self . strategy = strategy
    self . hand     = []
    self . inPlay   = True

  def getHandValue(self):
    value = 0
    for item in self . hand:
      if item[1] == 'J' or item[1] == 'K' or item[1] == 'Q':
        value += 1
        continue
      if item[1] == '7':
        value += 7
        continue
      if item[1] == '8':
        value += 8
        continue
      if item[1] == '9':
        value += 9
        continue
      if item[1:] == '10':
        value += 10
        continue
    return value

  def acceptCard( self, cards ):
    if self.needsCard():
      self.hand.append( cards[0] )
      cards.remove( cards[0] )

  def needsCard(self):
    if self . strategy == 'Human':
      print( f"{self.name} has these cards: {self.hand} with value: {self.getHandValue()}." )
      play = input( "Hit or stand? (h/s)" )
      if play == 'h':
        return True
    if self . strategy == 'Cautious':
      if self . getHandValue() < 10:
        return True
    if self . strategy == 'Bold':
      if self . getHandValue() < 15:
        return True
    return False
# TEST DEAL

dealer = Dealer()
dealer.shuffle()
myHand = dealer.deal(5)
print(myHand)
dealer.shuffle()
myHand = dealer.deal(3)

print(myHand)

# TEST GAME

newDealer = Dealer()
player1 = Player('Čeněk Člověčí', 'Human')
player2 = Player('Vilda Vopatrný', 'Cautious')
player3 = Player('Olda Odvážný','Bold')
newDealer.addPlayer(player1)
#newDealer.addPlayer(player2)
#newDealer.addPlayer(player3)
newDealer.shuffle()
newDealer.players[0].hand = newDealer.deal( 5 )
print( newDealer.players[0].hand )
print( newDealer.players[0].getHandValue() )
newDealer.startRound()