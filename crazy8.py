#Azaan Dawson
import math
import random
import time
import turtle

def play_game(cards):
    player_selection = input("Welcome to Cazy 8s.\nWould you like to play two player mode? y for yes n for no: ")
    if player_selection == "n":
        player1_cards = random.choices(cards,k=8)
        computer_cards = random.choices(cards,k=8)
        card_down = random.choice(cards)
        card_down_list = card_down.split(' ')
        while True:
            if len(computer_cards)==0:
                break
            else:
                while True:
                    player1_play = input("The card down is "+card_down+". You have "+str(player1_cards)+" in your hand. Which would you like to play?\nIf you'd like to pick up a card, input pickup\n")
                    player1_play_list = player1_play.split(' ')
                    if player1_play== 'pickup':
                        player1_cards.append(random.choice(cards))
                        break    
                    elif player1_play_list[0]== card_down_list[0] or player1_play_list[1] == card_down_list[1]:
                        if player1_play_list[1] == '2':
                            computer_cards.append(random.choices(cards, k=2))
                            player1_cards.remove(player1_play)
                            card_down = player1_play
                            card_down_list = player1_play_list
                            continue
                        elif player1_play_list[1] == '4' or 'Ace':
                            player1_cards.remove(player1_play)
                            card_down = player1_play
                            card_down_list = player1_play_list
                            continue
                        elif player1_play_list[1] == '9':
                            player1_cards.remove(player1_play)
                            card_down = player1_play
                            card_down_list = player1_play_list
                            continue
                        elif player1_play == 'spades Queen':
                            computer_cards.append(random.choices(cards,k=5))
                            player1_cards.remove(player1_play)
                            card_down = player1_play
                            card_down_list = player1_play_list
                            continue
                        else:
                            player1_cards.remove(player1_play)
                            card_down = player1_play
                            card_down_list = player1_play_list
                            break
                    else:        
                        print("This card cannot be placed here")
                if len(player1_cards) == 0:
                    break
                else:
                    while True:
                        print("works")
                        break             
cards= ['hearts 2','hearts 3','hearts 4','hearts 5', 'hearts 6', 'hearts 7', 'hearts 8', 'hearts 9', 'hearts 10', 'hearts Jack', 'hearts Queen', 'hearts King', 'hearts Ace', 'spades 2', 'spades 3', 'spades 4', 'spades 5', 'spades 6', 'spades 7', 'spades 8', 'spades 9', 'spades 10', 'spades Jack', 'spades Queen', 'spades King', 'spades Ace', 'diamonds 2', 'diamonds 3', 'diamonds 4', 'diamonds 5', 'diamonds 6', 'diamonds 7', 'diamonds 8', 'diamonds 9', 'diamonds 10', 'diamonds Jack', 'diamonds Queen', 'diamonds King', 'diamonds Ace', 'clubs 2', 'clubs 3', 'clubs 4', 'clubs 5', 'clubs 6', 'clubs 7', 'clubs 8', 'clubs 9', 'clubs 10', 'clubs Jack', 'clubs Queen', 'clubs King', 'clubs Ace']
play_game(cards)