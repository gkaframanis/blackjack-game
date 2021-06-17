############### Blackjack Project #####################
############### Our Blackjack House Rules #############

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from art import logo


def user_first_cards(cards):
    user_cards = []
    for _ in range(2):
        user_cards.append(random.choice(cards))
    return user_cards


def dealer_first_card(cards):
    dealer_cards = []
    dealer_cards.append(random.choice(cards))
    return dealer_cards


def count_score(cards):
    score = sum(cards)
    if 11 in cards and score > 21:
        score -= 10
    return score


def deal_card(cards):
    return random.choice(cards)


def compare_dealer_score(dealer_score, score):
    if dealer_score > 21:
        print("Dealer went over! You win!")
    elif dealer_score > score:
        print("Dealer has better hand! You lose!")
    elif dealer_score < score:
        print("You have better hand! You win!")
    else: 
        print("Draw!")


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

keep_playing_blackjack = True
while keep_playing_blackjack:
    answer = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    if answer == "y":
        print(f"{logo}\n")

        user_cards = user_first_cards(cards)
        user_score = count_score(user_cards)

        dealer_cards = dealer_first_card(cards)
        dealer_score = count_score(dealer_cards)

        print(f"Your cards {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {dealer_cards}")

        choice = "y"
        while user_score < 21 and choice == "y":
            choice = input("Type 'y' to get another card, type 'n' to pass: ")
        
            if choice == "y":
                user_cards.append(deal_card(cards))
                user_score = count_score(user_cards)
                print(f"Your cards {user_cards}, current score: {user_score}")
                if user_score == 21:
                    print("BlackJack! You win!!!")
                if user_score > 21:
                    print("You went over... You lose!") 

            else:
                while dealer_score < 17:
                    dealer_cards.append(deal_card(cards))
                    dealer_score = count_score(dealer_cards)
                    print(f"Computer's cards {dealer_cards}, computer's current score: {dealer_score}")

        compare_dealer_score(dealer_score, user_score)

    else:
        keep_playing_blackjack = False







