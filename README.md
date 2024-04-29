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

