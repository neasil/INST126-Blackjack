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
             "Ace of Clubs": 11}

# Tracking wins for players and dealer
p1_wins = 0
p2_wins = 0
dealer_wins = 0

# Functions: 
def player_ace(card_drawn):
    """
    Used only for players. Allows them to choose whether Ace equals to 1 or 11.
    """
    ace = input("You have drawn an Ace. Would you like it to equal 1 or 11?\t")
    if ace == str(1):
      card_drawn = 1
      print("For this draw, Ace equals {}".format(ace))
      return card_drawn
    elif ace == str(11):
      card_drawn = 11
      print("For this draw, Ace equals {}".format(ace))
      return card_drawn  
    else:
      print("It seems that you've entered an invalid input.")
      return player_ace(card_drawn)
    
def dealer_ace(card_drawn):
    """
    Used only for the dealer. Automatically determines whether Ace is equal to 1 or 11 based on Blackjack conventions.
    """
    total = dealer_draw(card_deck)
    if total >= 10:
      card_drawn = 1
      print("For this draw, Ace equals {}".format(card_drawn))
      return card_drawn 
    else:
      card_drawn = 11
      print("For this draw, Ace equals {}".format(card_drawn))
      return card_drawn

def player_draw(deck, player):
    """
    Simulates a player drawing a card.
    """
    card = random.choice(list(deck))
    print("{} drew ".format(player) + str(card))
    if "ace" in card.lower():
      card_value = player_ace(card)
    else: 
      card_value = deck[card]
    del card_deck[card]
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
             "Ace of Clubs": 11}
    hand = []
    hand = np.append(hand, card_value)
    return hand  

def dealer_draw(deck):
    """
    Simulates the dealer drawing a card. 
    """
    card = random.choice(list(deck))
    print("Dealer drew " + str(card))
    if "ace" in card.lower():
      card_value = dealer_ace(card)
    card_value = deck[card]
    del card_deck[card]
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
             "Ace of Clubs": 11}
    hand = []
    hand = np.append(hand, card_value)
    return hand
 
def manual_play(player_input, player_score, player_id):
    """
    Used after the initial 2 card draws. Allows for players to 'hit' or 'stay' as many times as they'd like to. 
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
    
def score(player, card_1, card_2):
    """
    Calculates final scores for initial 2 draws. 
    """
    print("Tallying current score for {}...\n".format(player))
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







