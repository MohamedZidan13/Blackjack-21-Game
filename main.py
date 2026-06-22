import random
import os
import time 
total_player = 0
while True :
  print("\nChoose a game to start........\n")
  Game = input("""1- Froggy
2- Twenty one 
3- snake 
__________\n""").capitalize()
  if Game == "Twenty one" :
    os.system("cls" if os.name=="nt" else "clear")
    print("Starting Game.........\n")
    time.sleep(2)
    print("""            _____
           |A .  | _____
           | /.\ ||A ^  | _____
           |(_._)|| / \ ||A _  | _____
           |   |  || \ / || ( )||A_ _ |
           |____V||  .  ||(_'_)||( v )|
                  |____V||  |  || \ / |
                         |____V||  .  |
                                |____V|\n""")
    print("_____________________________________________________________\n")
  #def game(turn):
       
       
  def Deal_card() :
              cards = [11,2,3,4,5,6,7,8,9,10,10,10]
              card =random.choice(cards)
              return card
  def total(cards):
              if sum(cards) == 21 and len(cards) == 2:
                 return 0
              if 11 in cards and sum(cards) > 21 :
                 cards.remove(11)
                 cards.append(1)
              return sum(cards)

  def compare(user_score,computer_score):
                 results = {
                    "Draw": "Draw😊\n\n",
                    "user_over": "You went over 21, Sorry🫢\n\n ",
                    "computer_over": "Computer went over 21, you win ⭐️\n\n",
                    "user_21" : "You won with a blackjack 😎👌\n\n",
                    "compuet_21": "Sorry, Computer had a blackjack 😱 \n\n",
                    "user_win": "you win 🥰 \n\n",
                    "user_lose": "You lose 😥 \n\n",            
                 }
                 if user_score == computer_score :
                    return results["Draw"]
                 elif user_score > 21:
                    return results["user_over"]
                 elif computer_score > 21:
                    return results["computer_over"]
                 elif user_score == 0:
                    return results["user_21"]  
                 elif computer_score == 0 :
                    return results["compuet_21"]
                 elif user_score > computer_score:
                    return results["user_win"]
                 elif user_score < computer_score:
                    return results["user_lose"]
                    
                    
  def Game1():  
    chosen_cards_player = [Deal_card() for i in range(2)]
    chosen_cards_computer = [Deal_card() for i in range(2)]
    game_continue = True
    while game_continue == True :
       user_score = total(chosen_cards_player)
       computer_score = total(chosen_cards_computer)
       print(f"\n\n\n Your cards are {chosen_cards_player}, current score is {sum(chosen_cards_player)}")
       print(f"computer's firt card is {chosen_cards_computer[0]}")
       if user_score == 0 or computer_score == 0 or user_score > 21 or computer_score > 21 :
          game_continue = False
       else :
          user_needs_another_card = input("Get another card? (y/n): ").lower()
          if user_needs_another_card == "y":
             chosen_cards_player.append(Deal_card())
          else :
             game_continue = False
    while sum(chosen_cards_computer) != 0 and sum(chosen_cards_computer) < 17 :
       chosen_cards_computer.append(Deal_card())
       computer_score = total(chosen_cards_computer)
    print(f"Your final hand {chosen_cards_player} with score {sum(chosen_cards_player)}")
    print(f"computer's final hand is {chosen_cards_computer} with score {sum(chosen_cards_computer)} ")
    print(compare(sum(chosen_cards_player),sum(chosen_cards_computer)))  
  if Game == "Twenty one" :
    Game1()
