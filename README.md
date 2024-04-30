# BlackJack-variant
This is one of the BlackJack variants - card game played in casinos.

The purpose of this project is to simulate the Casino BJc game in python, and reveal how this valiant of BJc is hugely in favor of house, so people avoide playing this valiant of BJc.
Here's how the rules are set by casino and how it's played.

Input:
	input("num_players = ?")
	input("table_rounds = ?)

- Face cards are replaced with 10
- Cards are dealt 1-by-1 clockwise, Each player is dealt two cards while dealer receives one. (players 2:1 dealer)
- if 2 cards sum=21 --> BJc, chuck'em into directHand if dealer card != 'A' or '10'

Split (upto 2 times):
	Always split pair of 'A' & '8'
	split pair of 2,3,4,6,7 & 9 Vs. 4,5,6

Hit against Dealer card:
	if Dealer card is 2 or 3, Hit upto 13
	if Dealer card is 4, 5 or 6 Hit upto 12
	Else, Hit upto 17

Double-Down:
	Always on 11
	Double on 10 except dealer has 'A' or '10'
	Double on 9 Vs. dealer card 3, 4, 5 or 6

SoftHand (A==11):
	A+7 DoubleDown Vs. Dealer <= 6 & Hit Vs. 'A', 9 or 10
	A+6 DoubleDown Vs. 3,4,5,6 & Else Hit
	A+2,3,4,5 DoubleDown Vs. 5,6 & Else Hit

DirectHands:
	sum >= 21
	5cards <= 21 [obvious: len(player) == 4 and total(player) < 12, deal 1 more card. 'A' values 1]

- If all the players are out no more card required on dealer
- played_hands are arranged as below order. Than, append back into the Shoe.
	played_hands = [dealer_hand + reversed(stay_hands) + direct_hands]


===================================

There are 3 aspects of the game
	1. Shoe: Initially, Six Decks of cards, randomly shuffled are loaded here
	2. Table: deal 2 cards to players and 1 card to dealr. Then, play according to Dealer's first card
	3. Rack: Played cards are chucked in here, then appended back to the Shoe in every round


OutPut:
	P1: [2,5,10]	 = 17 (Loose)
	P2: [10,A]	 = 21 (Bjc)
	P3: [7,4,10]	 = 21 (Bust)
	P4: [2,3,2,A,10] = 20 (Win)
	P5: [6,6,10]	 = 22 (Bust)
	P6: [8,10]	 = 18 (Tie)
	P7: [6,5,3]	 = 14 (Loose)
	D: [7,A]	 = 17

Final card arrangement in the Shoe: [8,2,7,9,7,5,10,8,4,6,6,10,7,3,6,10,10,4,10,10,2,10,5,2,10,10,10,5,7,2,7,10,5,A,4,6,8,A,10,7,8,3,4,6,10,3,7,10,7,A,5,9,8,6,7,10,10,9,A,10,9,10,10,10,3,A,10,10,A,9,6,10,8,4,6,10,10,2,8,6,2,A,5,5,10,5,8,9,2,2,3,10,10,10,10,10,7,4,3,10,4,A,A,A,8,10,10,10,10,10,10,10,9,6,10,2,3,10,7,5,3,8,A,10,4,10,8,A,9,8,10,10,4,10,A,2,9,7,10,4,5,A,2,10,10,7,A,A,7,9,8,A,9,10,8,6,4,9,10,10,4,10,3,3,3,10,2,2,10,10,10,6,3,8,10,7,10,10,6,5,10,3,9,3,10,4,5,8,10,3,10,7,10,3,2,5,10,4,4,9,9,9,4,10,5,10,2,5,4,6,4,8,8,6,7,10,10,10,10,6,9,2,10,6,9,10,2,6,4,10,A,10,10,3,2,2,A,A,5,3,9,10,3,2,10,3,10,6,10,A,5,10,4,A,A,5,5,8,5,2,10,8,10,10,8,6,5,10,10,6,3,9,10,9,3,2,3,4,3,5,10,A,4,7,9,8,6,10,5,10,10,7,4,7,8,10,5,10,2,7,7,10,9,4,2,6,9,7,8,10,6,7]

