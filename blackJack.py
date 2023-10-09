#Nathan Curl
#04/19/22

import random
import time

playerIn = True
dealerIn = True

# deck of cards; the player's and dealer's hand
deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10, 2, 3, 4, 5, 6, 7, 8, 9, 10,
        "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A", "J", "Q", "K", "A"]
playerHand = []
dealerHand = []

#Big Game Loop
print("Ready to play some Blackjack?")
user_input = input("1: Yes\n2: No\n")
if user_input.lower() != "yes":
    print("You would've lost anyway.")
    exit()
else:
    while True:

    #dealing the cards:

        def cardDealing(turn):
        #first choose a random card from the deck to form both dealer and player hands
            card = random.choice(deck)
        #add selected card to the list belonging to who's turn it is
            turn.append(card)
        #remove chosen card from list labeled "deck"
            deck.remove(card)

    #calculate the total of each hand:

        def totalHand(turn):
            total = 0
            face = [ "J", "Q", "K"]
            for card in turn:
                if card in range(1,11):
                    total += card
                elif card in face:
                    total += 10
                else:
                    if total > 11:
                        total += 1
                    else:
                        total += 11
            return total

    #Checking who won?:

        def revealDealer():
            if len(dealerHand) == 2:
                return dealerHand[0]
            elif len(dealerHand) > 2:
                return dealerHand[0], dealerHand[1]

    #Loop for the game:

        for _ in range(2):
            cardDealing(dealerHand)
            cardDealing(playerHand)

        while playerIn or dealerIn:
            print(f"Dealer has {revealDealer()} and X")
            print(f"You have {playerHand} for a total of {totalHand(playerHand)}")
            if playerIn:
                stayOrHit = input("1: Stay\n2: Hit\n")
            if totalHand(dealerHand) > 16:
                dealerIn = False
            else:
                cardDealing(dealerHand)
            if stayOrHit.lower() == "stay":
                playerIn = False
            else:
                cardDealing(playerHand)
            if totalHand(playerHand) >= 21:
                break
            elif totalHand(dealerHand) >= 21:
                break
        if totalHand(playerHand) == 21:
            print(f"\nYou have {playerHand} for a total of {totalHand(playerHand)} and the dealer has {dealerHand} for a total of {totalHand(dealerHand)}")
            time.sleep(2)
            print("Congrats! You got Blackjack! Good win.")
            time.sleep(2)
            # print("Want to play again?")
        elif totalHand(dealerHand) == 21:
            print(f"\nYou have {playerHand} for a total of {totalHand(playerHand)} and the dealer has {dealerHand} for a total of {totalHand(dealerHand)}")
            time.sleep(2)
            print("Unlucky :( The dealer got Blackjack. You lost.")
            time.sleep(2)
            # print("Want to play again?")
        elif totalHand(playerHand) > 21:
            print(f"\nYou have {playerHand} for a total of {totalHand(playerHand)} and the dealer has {dealerHand} for a total of {totalHand(dealerHand)}")
            time.sleep(2)
            print("You busted, the Dealer won.")
            time.sleep(2)
            # print("Want to play again?")
        elif totalHand(dealerHand) > 21:
            print(f"\nYou have {playerHand} for a total of {totalHand(playerHand)} and the dealer has {dealerHand} for a total of {totalHand(dealerHand)}")
            time.sleep(2)
            print("The dealer busted. You win!")
            time.sleep(2)
            # print("Want to play again?")
        elif 21 - totalHand(dealerHand) < 21 - totalHand(playerHand):
            print(f"\nYou have {playerHand} for a total of {totalHand(playerHand)} and the dealer has {dealerHand} for a total of {totalHand(dealerHand)}")
            time.sleep(2)
            print("Unlucky. The dealer wins.")
        elif 21 - totalHand(dealerHand) > 21 - totalHand(playerHand):
            print(f"\nYou have {playerHand} for a total of {totalHand(playerHand)} and the dealer has {dealerHand} for a total of {totalHand(dealerHand)}")
            time.sleep(2)
            print("Congrats. You win!")

        print("Wanna play again?")
        play_again = input("1: Yes\n2: No\n")
        if play_again.upper() != "YES":
            print("thank you for playing!")
            break
        else:
            playerIn = True
            total = 0
            # for card in playerHand:
            #     card.append(deck)
            #     playerHand.remove(card)
            # for card in dealerHand:
            #     card.append(deck)
            #     dealerHand.remove(card)
            playerHand.clear()
            dealerHand.clear()