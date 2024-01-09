# User Requirements:
# 1. Simulate rounds of (non-betting) Blackjack, where each player is dealt a card from a standard
#    52-card deck, such that duplicate cards cannot be drawn until the entire deck is drawn (and
#    “re-shuffled”).
# 2. If a player busts, they lose immediately.
# 3. Each player can choose to “hit” (draw a card) or “stay”.
# 4. When a player chooses “stay”, their total is set until the round is over, and cannot choose to “hit”
#    again that round.
# 5. If multiple players “stay”, the highest total wins. 
# 6. The game could be designed to be played “manually” or “automatically”
#      • “Manually” means one or both (human) players making choices one by one.
#      • “Automatically” means that both player’s choices should be made automatically, by some
#         kind of rule or algorithm implemented in the program.
# 7. Should be able to run many automatic games. 

# Notes:
# 1. No betting.
# 2. All cards in play are visible.
# 3. Start with two players. 

# Steps:
# * Will be played manually
# 1. Make an array to represent the 52-card deck. Face cards are equal to 10. 4 suits (Heart, Diamond, Spade, Club) 
#    and 13 cards in each suit. In this case, suits don't matter. The 13 cards are Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
#    Jack, Queen, King
# 2. Ask users for what value they want Ace to be (1 or 11) with input statement. Set this input to the ace variable for
#    each user.
# 3. "Shuffle" the deck and deal a card to the player using np.random.choice without replacement. Store in a variable 
#     and print result.
# 4. The program will draw a card. Store this in a variable. Print out what was drawn.
# 5. Players are each dealt another card. Store this in another variable. Print out what they got. 
# 6. Program draws another a card. Store in variable. Print what was drawn. 
# 7. Check if anyone already reached 21 (natural/blackjack). If a player did but the dealer didn't, the player wins. 
#    If the dealer did, but the players don't, the dealer "wins."" If both the dealer and a player achieve a natural, 
#    it's a tie and neither of them win.
# 8. If no one has achieved a natural, we proceed with the game. 
# 9. Prompt player 1 for if they want to "hit" (draw another card) or "stay" (keep their current hand).
# 10. If player 1 chooses to hit, draw another card from the deck. Prompt again. This should loop until they "stay."
# 11. If player 1 chooses to stay, end their turn. 
# 12. Do the same for player 2. 
# 13. Count the value of each player's hand. If the value exceeds 21, they automatically lose or "bust."
# 14. Count the value of the dealer's hand and compare it the hands of both players. If the dealer is closer to 21, 
#     the dealer wins. If not, the dealer loses. Either one of the players who is closer to 21 wins. 
# 15. Output the result of this round.
# 16. There should be a way to keep track of how many times each player wins. 
# 16. Prompt the user if they want to play again. "continue" or "quit."

import numpy as np

print("Welcome to this Blackjack simulator! This is a two-player game that does not use betting, so no worries about losing money! All cards in play will be visible to all players.\n")

# Defining Ace for each player
# Actually, Ace value changes depending on whether or not it will give the player a bust so it isn't defined
# at the beginning...haha

# How many times to play 
print("You can play as many rounds as you'd like. At the end of every round, you will be prompted to continue or quit. Please follow the on-screen prompt to indicate your choice.\n")
play = input("Would you like to play? Please type 'yes' to continue or anything else to quit.\t").lower()

try:
    play == "yes" or play == "no"
except: 
    print("Hmmm it appears you entered an invalid input.")
    play = input("Would you like to play? Please type 'yes' to continue or 'no' to quit.\t").lower()

 # Tracking wins
p1_wins = 0
p2_wins = 0
dealer_wins = 0

while play == "yes":
    ace_1 = 11
    ace_2 = 11
    # Setting up card decks as lists 
    ace = 11
    jack = 10
    queen = 10
    king = 10
    
    card_deck_1 = [ace_1, ace_1, ace_1, ace_1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 
            8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, jack, jack, jack, jack, queen, queen, queen, queen, king, king, king, king]
    card_deck_2 = [ace_2, ace_2, ace_2, ace_2, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 
            8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, jack, jack, jack, jack, queen, queen, queen, queen, king, king, king, king]
    dealer_deck = [ace, ace, ace, ace, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 
            8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, jack, jack, jack, jack, queen, queen, queen, queen, king, king, king, king]
    
    # Starting the game 
    print("Now that we're all set, let's open the game!!\n")
    print("The dealer has started dealing...\n")
    
    # 1st draw:
    # Player 1
    p1_card1 = np.random.choice(card_deck_1, replace=False)
    print("Player 1 was dealt " + str(p1_card1))
    player_1 = []
    player_1 = np.append(player_1, p1_card1)
    
    # Player 2
    p2_card1 = np.random.choice(card_deck_2, replace=False)
    print("Player 2 was dealt " + str(p2_card1))
    player_2 = []
    player_2 = np.append(player_2, p2_card1)
    
    # Dealer
    dealer_card1 = np.random.choice(dealer_deck, replace=False)
    print("The dealer drew " + str(dealer_card1))
    dealer = []
    dealer = np.append(dealer, dealer_card1)
    print("Time for the second draw!\n")
    
    # 2nd draw:
    # Player 1
    p1_card2 = np.random.choice(card_deck_1, replace=False)
    print("Player 1 was dealt " + str(p1_card2))
    player_1 = np.append(player_1, p1_card2)
    
    # Player 2
    p2_card2 = np.random.choice(card_deck_2, replace=False)
    print("Player 2 was dealt " + str(p2_card2))
    player_2 = np.append(player_2, p2_card2)
    
    # Dealer
    dealer_card2 = np.random.choice(dealer_deck, replace=False)
    print("The dealer drew " + str(dealer_card2))
    dealer = np.append(dealer, dealer_card2)
    
    # Results of first two draws: 
    print("Tallying current scores...\n")
    
    # Scores: 
    p1_score = sum(player_1)
    p2_score = sum(player_2)
    dealer_score = sum(dealer)
    print("Player 1 now has a total of " + str(p1_score))
    print("Player 2 now has a total of " + str(p2_score))
    print("The dealer now has a total of " + str(dealer_score))
    
    # Check if anyone has already hit a Blackjack. 
    #if p1_score == 21: 
        #print("Player 1 has achieved Blackjack!")
        #p1_wins += 1
    #elif p2_score == 21:
        #print("Player 2 has achieved Blackjack!")
        #p2_wins += 1
    #elif dealer_score == 21:
        #dealer_wins += 1
        #print("The dealer has achieved Blackjack!")
    #elif p1_score == 21 and p2_score == 21:
        #print("It's a tie! Neither Player 1 or Player 2 win.")
        
    # Player 1's turn:
    print("\n")
    p1_draw = input("Player 1: Would you like to hit or stay? Please type 'hit' or 'stay': \n").lower()
    
    try:
        p1_draw == "stay" or p1_draw == "hit"
    except: 
        print("Hmm it seems you didn't enter a valid input.")
        p1_draw = input("Player 1: Would you like to hit or stay? Please type 'hit' or 'stay': \n").lower()

    if p1_draw == "stay":
        print("Stay. Player 1's hand is sealed. Player 1 now has a total of {}".format(p1_score))
    elif p1_draw == "hit":
        while p1_draw == "hit":
            print("Hit. You have been dealt another card.")
            p1_card = np.random.choice(card_deck_1, replace=False)
            print("Player 1 was dealt " + str(p1_card))
            player_1 = np.append(player_1, p1_card)
            p1_score = sum(player_1)
            print("Player 1 now has a count of {}".format(p1_score))
            print("\n") 
            # Checking for Blackjack or surpassing 21
            if p1_score > 21:
                print("Uh oh! Player 1's total has surpassed 21 and reached {}! Player 1 looses this round.".format(p1_score))
                break
            elif p1_score == 21:
                print("Wow! Player 1 has achieved Blackjack.")
                break
            p1_draw = input("Player 1: Would you like to hit or stay? Please type 'hit' or 'stay': \t").lower()
            if p1_draw == "stay":
                print("Stay. Player 1's hand is sealed. Player 1 now has a total of {}".format(p1_score))
                print("\n")
                
    # Player 2's turn:
    p2_draw = input("Player 2: Would you like to hit or stay? Please type 'hit' or 'stay': \n").lower()

    try:
        p2_draw == "stay" or p2_draw == "hit"
    except: 
        print("Hmm it seems you didn't enter a valid input.")
        p2_draw = input("Player 2: Would you like to hit or stay? Please type 'hit' or 'stay': \n").lower()
    
    if p2_draw == "stay":
        print("Stay. Player 2's hand is sealed. Player 2 now has a count of {}".format(p2_score))
    elif p2_draw == "hit":
        while p2_draw == "hit":
            print("Hit. You have been dealt another card.")
            p2_card = np.random.choice(card_deck_2, replace=False)
            print("Player 2 was dealt " + str(p2_card))
            player_2 = np.append(player_2, p2_card)
            p2_score = sum(player_2)
            print("Player 2 now has a total of {}".format(p2_score))
            # Checking for Blackjack or surpassing 21
            if p2_score > 21:
                print("Uh oh! Player 2's total has surpassed 21 and reached {}! Player 2 looses this round.".format(p2_score))
                break 
            elif p2_score == 21:
                print("Wow! Player 2 has hit Blackjack!")
                break
            p2_draw = input("Player 2: Would you like to hit or stay? Please type 'hit' or 'stay': \t").lower()
            if p2_draw == "stay":
                print("Stay. Player 2's hand is sealed. Player 2 now has a count of {}.".format(p2_score))
                
    # Dealer's turn: 
    print("\n")
    print("The dealer will now play.")

    if dealer_score >= 17:
        print("The dealer's total is {}. They must stand.".format(dealer_score))
    else:
        print("The dealer's total is below 17. They must hit.")
        while dealer_score <= 17:
            dealer_card3 = np.random.choice(dealer_deck, replace=False)
            print("The dealer drew " + str(dealer_card2))
            dealer = np.append(dealer, dealer_card2)
            dealer_score = sum(dealer)
            print("The dealer now has a total of {}.".format(dealer_score))
            if dealer_score > 21: 
                print("Uh oh! The dealer's total has exceeded 21 and reached {}! The dealer loses this round.".format(dealer_score))
    
    # Checking who won
    if p1_score > p2_score and p1_score > dealer_score:
        if p1_score <= 21:
            p1_wins += 1
            print("Congratulations! Player 1 wins this round.")
            print("Player 1 has now won {} times".format(p1_wins))
        else: 
            break
    elif p2_score > p1_score and p2_score > dealer_score: 
        if p2_score <= 21:
            p2_wins += 1
            print("Congratulations! Player 2 wins this round.")
            print("Player 2 has now won {} times".format(p2_wins))
        else: 
            break
    elif dealer_score > p1_score and dealer_score > p2_score:
        if dealer_score <= 21:
            dealer_wins += 1
            print("Rats! The dealer won this round. Neither Player 1 or 2 win.")
            print("The Dealer has now won {} times".format(dealer_wins))
        else:
            break
    else:
        print("It looks like no one won this round...")

    # Continue or quit?
    play = input("Would you like to continue playing? Please type 'yes' to continue or 'no' to quit. \t").lower()

    # Output results
    if play == "no":
        print("You have chosen to quit. ")
        print("Here are the final results: \n")
        print("Player 1 won {} times.".format(p1_wins))
        print("Player 2 won {} times.".format(p2_wins))
        print("The dealer won {} times.".format(dealer_wins))







