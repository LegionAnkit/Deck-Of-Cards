from random import shuffle

class Card:
	
	def __init__(self,value,suit):
		allowed_suit=["Heart","Club","Diamond","Spade"]
		allowed_value=["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
		if suit not in allowed_suit:
			raise ValueError(f"Card can only have suit from {allowed_suit}")
		if value not in allowed_value:
			raise ValueError(f"Card can only have suit from {allowed_value}")
		self.suit=suit
		self.value=value

	def __repr__(self):
		return f"{self.value} of {self.suit}"

# card= Card("A", "Heart")
# print(card)

class Deck:

	def __init__(self):
		suits = ["Heart","Club","Diamond","Spade"]
		values = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
		self.cards= [Card(value,suit) for suit in suits for value in values]
		

	def __repr__(self):
		return f"Deck of {self.count()} cards"
	
	def count(self):
		return len(self.cards)		

	def _deals(self,num):
		count= self.count()
		deals= min([count,num])
		if count==0:
			raise ValueError("All cards have been dealt")
		cards= self.cards[-deals:]
		self.cards=self.cards[:-deals]
		return cards

	def deal_card(self):
		return self._deals(1)[0]

	def deal_hand(self,num):
		return self._deals(num)

	def shuffle(self):
		if self.count() < 52:
			raise ValueError("Only full decks can be shuffled")
		shuffle(self.cards)
		return self


d = Deck()
d.shuffle()
card = d.deal_card()
print(card)
hand = d.deal_hand(50)
card2 = d.deal_card()
print(card2)
print(d.cards)
card2 = d.deal_card()


