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

# Import statements:
import numpy as np
import random

# Welcome message!
print("Welcome to this Blackjack simulator! This is a two-player game that does not use betting, so no worries about losing money! All cards in play will be visible to all players.\n")

# Letting the player know that they can play as many times as they want to
print("You can play as many rounds as you'd like. At the end of every round, you will be prompted to continue or quit. Please follow the on-screen prompt to indicate your choice.\n")

# Asking the player if they want to play
play = input("Would you like to play? Please type 'yes' to continue or anything else to quit.\t").lower()

# Setting up the card deck 
#https://www.programiz.com/python-programming/methods/dictionary/fromkeys
card_deck = {"Jack of Hearts":10,
             "Jack of Diamonds":10,
             "Jack of Spades":10,
             "Jack of Clubs":10, 
             "Queen of Hearts":10,
             "Queen of Diamonds":10,
             "Queen of Spades":10,
             "Queen of Clubs":10,
             "King of Hearts":10,
             "King of Diamonds":10,
             "King of Spades":10,
             "King of Clubs":10,
             "2 of Hearts":2,
             "2 of Diamonds":2,
             "2 of Spades":2,
             "2 of Clubs":2,
             "3 of Hearts":3,
             "3 of Diamonds":3,
             "3 of Spades":3,
             "3 of Clubs":3,
             "4 of Hearts":4,
             "4 of Diamonds":4,
             "4 of Spades":4,
             "4 of Clubs":4,
             "5 of Hearts":5,
             "5 of Diamonds":5,
             "5 of Spades":5,
             "5 of Clubs":5,
             "6 of Hearts":6,
             "6 of Diamonds":6,
             "6 of Spades":6,
             "6 of Clubs":6,
             "7 of Hearts":7,
             "7 of Diamonds":7,
             "7 of Spades":7,
             "7 of Clubs":7,
             "8 of Hearts":8,
             "8 of Diamonds":8,
             "8 of Spades":8,
             "8 of Clubs":8,
             "9 of Hearts":9,
             "9 of Diamonds":9,
             "9 of Spades":9,
             "9 of Clubs":9,
             "Ace of Hearts": 11,
             "Ace of Diamonds": 11,
             "Ace of Spades": 11,
             "Ace of Clubs": 11
             }
print(card_deck)
# Tracking wins for players and dealer
p1_wins = 0
p2_wins = 0
dealer_wins = 0

# Functions: 
# To help players choose what value they would like Ace to be when drawn
def player_ace(ace_drawn):
    """
    Used only for players. Allows them to choose whether Ace equals to 1 or 11.

    Parameters: 
    ace_drawn (string): the Ace the player drew

    Returns: 
    ace_drawn (string): the player's current Ace
    """
    ace = input("You have drawn an Ace. Would you like it to equal 1 or 11?\t")
    if ace == str(1):
      ace_drawn = 1
      print("For this draw, Ace equals {}".format(ace))
      return ace_drawn
    elif ace == str(11):
      ace_drawn = 11
      print("For this draw, Ace equals {}".format(ace))
      return ace_drawn  
    else:
      print("It seems that you've entered an invalid input.")
      return player_ace(ace_drawn)

# Manually selects what value Ace will be for dealer when drawn
def dealer_ace(ace_drawn):
    """
    Used only for the dealer. Automatically determines whether Ace is equal to 1 or 11 based on Blackjack conventions.

    Arguments:
    ace_drawn (string): the Ace the dealer drew
 
    Returns:
    ace_drawn (string): the dealer's current Ace
    """
    total = dealer_draw(card_deck)
    if total >= 10:
      ace_drawn = 1
      print("For this draw, Ace equals {}".format(ace_drawn))
      return ace_drawn 
    else:
      ace_drawn = 11
      print("For this draw, Ace equals {}".format(ace_drawn))
      return ace_drawn

# For players to draw a card
def player_draw(deck, player):
    """
    Simulates a player drawing a card.

    Arguments:
    deck (dictionary): the card deck
    player (string): player 1 or 2
 
    Returns:
    hand (array): the player's current hand
    """
    card = random.choice(list(deck))
    print("{} drew ".format(player) + str(card))
    if "ace" in card.lower():
      card_value = player_ace(card)
    else: 
      card_value = deck[card]
    del card_deck[card]
    # Reshuffles the deck if all cards have been drawn
    if len(deck) == 0:
       deck = {"Jack of Hearts":10,
             "Jack of Diamonds":10,
             "Jack of Spades":10,
             "Jack of Clubs":10, 
             "Queen of Hearts":10,
             "Queen of Diamonds":10,
             "Queen of Spades":10,
             "Queen of Clubs":10,
             "King of Hearts":10,
             "King of Diamonds":10,
             "King of Spades":10,
             "King of Clubs":10,
             "2 of Hearts":2,
             "2 of Diamonds":2,
             "2 of Spades":2,
             "2 of Clubs":2,
             "3 of Hearts":3,
             "3 of Diamonds":3,
             "3 of Spades":3,
             "3 of Clubs":3,
             "4 of Hearts":4,
             "4 of Diamonds":4,
             "4 of Spades":4,
             "4 of Clubs":4,
             "5 of Hearts":5,
             "5 of Diamonds":5,
             "5 of Spades":5,
             "5 of Clubs":5,
             "6 of Hearts":6,
             "6 of Diamonds":6,
             "6 of Spades":6,
             "6 of Clubs":6,
             "7 of Hearts":7,
             "7 of Diamonds":7,
             "7 of Spades":7,
             "7 of Clubs":7,
             "8 of Hearts":8,
             "8 of Diamonds":8,
             "8 of Spades":8,
             "8 of Clubs":8,
             "9 of Hearts":9,
             "9 of Diamonds":9,
             "9 of Spades":9,
             "9 of Clubs":9,
             "Ace of Hearts": 11,
             "Ace of Diamonds": 11,
             "Ace of Spades": 11,
             "Ace of Clubs": 11
             }
    hand = []
    hand = np.append(hand, card_value)
    return hand  

# For the dealer to draw a card
def dealer_draw(deck):
    """
    Simulates the dealer drawing a card. 

    Arguments:
    deck (dictionary): the card deck
 
    Returns:
    hand (list): the dealer's current hand
    """
    card = random.choice(list(deck))
    print("Dealer drew " + str(card))
    if "ace" in card.lower():
      card_value = dealer_ace(card)
    card_value = deck[card]
    del card_deck[card]
    # Reshuffles the deck if all cards have been drawn
    if len(deck) == 0:
       deck = {"Jack of Hearts":10,
             "Jack of Diamonds":10,
             "Jack of Spades":10,
             "Jack of Clubs":10, 
             "Queen of Hearts":10,
             "Queen of Diamonds":10,
             "Queen of Spades":10,
             "Queen of Clubs":10,
             "King of Hearts":10,
             "King of Diamonds":10,
             "King of Spades":10,
             "King of Clubs":10,
             "2 of Hearts":2,
             "2 of Diamonds":2,
             "2 of Spades":2,
             "2 of Clubs":2,
             "3 of Hearts":3,
             "3 of Diamonds":3,
             "3 of Spades":3,
             "3 of Clubs":3,
             "4 of Hearts":4,
             "4 of Diamonds":4,
             "4 of Spades":4,
             "4 of Clubs":4,
             "5 of Hearts":5,
             "5 of Diamonds":5,
             "5 of Spades":5,
             "5 of Clubs":5,
             "6 of Hearts":6,
             "6 of Diamonds":6,
             "6 of Spades":6,
             "6 of Clubs":6,
             "7 of Hearts":7,
             "7 of Diamonds":7,
             "7 of Spades":7,
             "7 of Clubs":7,
             "8 of Hearts":8,
             "8 of Diamonds":8,
             "8 of Spades":8,
             "8 of Clubs":8,
             "9 of Hearts":9,
             "9 of Diamonds":9,
             "9 of Spades":9,
             "9 of Clubs":9,
             "Ace of Hearts": 11,
             "Ace of Diamonds": 11,
             "Ace of Spades": 11,
             "Ace of Clubs": 11
             }
    hand = []
    hand = np.append(hand, card_value)
    return hand
 
# To allow the players to play
def manual_play(player_input, player_score, player_id):
    """
    Used after the initial 2 card draws. Allows for players to 'hit' or 'stay' as many times as they'd like to. 

    Arguments: 
    (string) player_input: whether or not the player 'hits' or 'stays'
    (int) player_score: the player's initial score
    (string) player_id: player 1 or 2


    Returns:
    (int) player_score: if the player decides to 'stay', the player's current score
    (int) new_score: if the player decides to 'hit', the player's redefined score
    """
    if player_input == "stay":
        print("Stay. {}'s hand is sealed. They now have a total of {}".format(player_id, player_score))
        return player_score
    elif player_input == "hit":
        while player_input == "hit":
            print("Hit. You have been dealt another card.")
            new_card = player_draw(card_deck, player_id)
            new_score = player_score + new_card
            if new_score > 21: # Checking for 'bust'
                print("Uh oh! {}'s total has surpassed 21 and reached {}! They lose this round.".format(player_id, new_score))
                return new_score
            elif new_score == 21: # Checking for Blackjack
                print("Wow! {} has achieved Blackjack.".format(player_id))
                return new_score
            print("You now have a score of " + str(new_score))
            print("\n") 
            player_input = input("{}: Would you like to hit or stay? Please type 'hit' or 'stay': \t".format(player_id)).lower()
            return manual_play(player_input, new_score, player_id)
    else: # If the player doesn't enter 'hit' or 'stay', they will be prompted to try again 
        player_input = input("Hmm it seems you entered an invalid input. {}: Would you like to hit or stay? Please type 'hit' or 'stay': \n".format(player_id)).lower()
        return manual_play(player_input, player_score, player_id)

# Used exclusively after the first 2 draws to help easily calculate scores by adding 2 card values together 
def score(player, card_1, card_2):
    """
    Calculates and prints out final scores for initial 2 draws. 
    
    Arguments:
    (string) player: player 1 or 2
    (int) card_1: first card drawn by player
    (int) card_2: second card drawn by player

    Returns:
    (array) total_score: calculated point value for player's current hand
    """
    total_score = card_1 + card_2
    print("{} now has a total of ".format(player) + str(total_score))
    return total_score

# Let the fun begin! 
while play == "yes": 
    
    # Starting the game 
    print("\n")
    print("Now that we're all set, let's open the game!!\n")
    print("The dealer has started dealing...\n")

    # 1st draw:
    # Player 1
    p1_card1 = player_draw(card_deck, "Player 1")
    
    # Player 2
    p2_card1 = player_draw(card_deck, "Player 2")
    
    # Dealer
    dealer_card1 = dealer_draw(card_deck)
    
    # 2nd draw:
    print("\n")
    print("Time for the second draw!\n")

    # Player 1
    p1_card2 = player_draw(card_deck, "Player 1")
    
    # Player 2
    p2_card2 = player_draw(card_deck, "Player 2")
    
    # Dealer
    dealer_card2 = dealer_draw(card_deck)
    type(p1_card1)
 
    # Results of first two draws: 
    print("\n")
    p1_score = score("Player 1", p1_card1, p1_card2) 
    p2_score = score("Player 2", p2_card1, p2_card2) 
    dealer_score = score("Dealer", dealer_card1, dealer_card2) 
    
    # Checking if anyone has already hit Blackjack
    if p1_score == 21: 
        if p2_score != 21 and dealer_score != 21:
            print("Player 1 has achieved Blackjack! Player 1 wins this round.")
            p1_wins += 1
    elif p2_score == 21:
        if p1_score != 21 and dealer_score != 21:
            print("Player 2 has achieved Blackjack! Player 2 wins this round.")
            p2_wins += 1
    elif dealer_score == 21:
        if p1_score != 21 and p2_score != 21:
            print("Dealer has achieved Blackjack! Dealer wins this round.")
            dealer_wins += 1
    elif p1_score == 21 and p2_score == 21:
        print("It's a tie! Neither Player 1 or Player 2 win.")
    else: 
        # Let us proceed! 
        # Player 1's turn:
        print("\n")
        p1_draw = input("Player 1: Would you like to hit or stay? Please type 'hit' or 'stay':\t").lower()

        p1_hand = manual_play(p1_draw, p1_score, "Player 1")
    
        # Player 2's turn:
        p2_draw = input("Player 2: Would you like to hit or stay? Please type 'hit' or 'stay':\t").lower()
    
        p2_hand = manual_play(p2_draw, p2_score, "Player 2")
                
        # Dealer's turn: 
        print("\n")
        print("The dealer will now play.")
        
        # Unlike the players, the dealer's draws are all automated
        if dealer_score >= 17:
            print("The dealer's total is {}. They must stand.".format(dealer_score))
        else: 
            print("The dealer's total is {}, which is below 17. They must hit.".format(dealer_score))
            while dealer_score <= 17:
               dealer_card = dealer_draw(card_deck)
               dealer_score = dealer_score + dealer_card
               print("The dealer now has a total of {}.".format(dealer_score))
               if dealer_score > 21: 
                   print("Uh oh! The dealer's total has exceeded 21 and reached {}! The dealer loses this round.".format(dealer_score))
                   break
    
        # Final scores: 
        print("\n")
        print("Player 1 now has a score of " + str(p1_hand)) 
        print("Player 2 now has a score of " + str(p2_hand))
        print("Dealer now has a score of " + str(dealer_score))     

        # Checking who won
        if p1_hand > 21:
            if p2_hand > dealer_score and p2_hand <= 21:
               p2_wins += 1
               print("Congratulations! Player 2 wins this round.")
            elif dealer_score > p2_hand and dealer_score <= 21:
               dealer_wins += 1
               print("Rats! The dealer won this round. Neither Player 1 or 2 win.")
            elif dealer_score > 21:
               p2_wins += 1
               print("Congratulations! Player 2 wins this round.")
            elif p2_hand > 21:
               dealer_wins += 1
               print("Rats! The dealer won this round. Neither Player 1 or 2 win.")
            else:
               print("It looks like no one won this round...")
        elif p2_hand > 21:
           if p1_hand > dealer_score and p1_hand <= 21: 
              p1_wins += 1
              print("Congratulations! Player 1 wins this round.")
           elif dealer_score > p1_hand and dealer_score <= 21:
              dealer_wins += 1
              print("Rats! The dealer won this round. Neither Player 1 or 2 win.")
           elif dealer_score > 21:
              p1_wins += 1
              print("Congratulations! Player 1 wins this round.")
           elif p1_hand > 21:
              dealer_wins += 1
              print("Rats! The dealer won this round. Neither Player 1 or 2 win.")
           else:
               print("It looks like no one won this round...")
        elif dealer_score > 21:
           if p1_hand > p2_hand and p1_hand <= 21:
               p1_wins += 1
               print("Congratulations! Player 1 wins this round.")
           if p2_hand > p1_hand and p2_hand <= 21:
               p2_wins += 1
               print("Congratulations! Player 2 wins this round.")
           elif p1_hand > 21:
              p2_wins += 1
              print("Congratulations! Player 2 wins this round.")
           elif p2_hand > 21:
              p1_wins += 1
              print("Congratulations! Player 1 wins this round.")
           else:
               print("It looks like no one won this round...")
        else:     
           if p1_hand > p2_hand and p1_hand > dealer_score:
              if p1_hand <= 21:
                p1_wins += 1
                print("Congratulations! Player 1 wins this round.")
           elif p2_hand > p1_hand and p2_hand > dealer_score: 
              if p2_hand <= 21:
                p2_wins += 1
                print("Congratulations! Player 2 wins this round.")
           elif dealer_score > p1_hand and dealer_score > p2_hand:
              if dealer_score <= 21:
                dealer_wins += 1
                print("Rats! The dealer won this round. Neither Player 1 or 2 win.")
           else:
               print("It looks like no one won this round...")

    # Continue or quit?
    play = input("Would you like to continue playing? Please type 'yes' to continue or anything else to quit.\t").lower()

    # Outputting results
    if play != "yes":
        print("You have chosen to quit. ")
        print("Here are the final results: \n")
        print("Player 1 won {} times.".format(p1_wins))
        print("Player 2 won {} times.".format(p2_wins))
        print("The dealer won {} times.".format(dealer_wins))







