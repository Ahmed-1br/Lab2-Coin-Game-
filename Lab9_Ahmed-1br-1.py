"""
Program Name: Match Coins Game - Main Program
Author: Ahmed Ibrahim
Purpose: Runs a two-player coin matching game
Starter Code: None
Date: September 27, 2026
"""

from player import Player

print("Welcome to the Match Coins Game!")

player1_name = input("Enter Player 1's name: ")
player2_name = input("Enter Player 2's name: ")

player1 = Player(player1_name)
player2 = Player(player2_name)

while player1.get_wallet() > 0 and player2.get_wallet() > 0:
    # Game logic would go here
    choice1 = input(f"\n{player1.get_name()}, choose Heads or Tails:")
    choice2 = input(f"\n{player2.get_name()}, choose Heads or Tails:")

    player1.toss_coin()
    player2.toss_coin()

    result1 = player1.get_coin_side()
    result2 = player2.get_coin_side()

    player1_correct = choice1.lower() == result1.lower()
    player2_correct = choice2.lower() == result2.lower()

    if player1_correct and not player2_correct:
        player1.win_coin()
        player2.lose_coin()

    elif player2_correct and not player1_correct:
        player2.win_coin()
        player1.lose_coin()

    else:
        print("No coins exchanged this round.")

    print(f"\n{player1.get_name()}'s coin landed on {result1}.")
    print(f"\n{player2.get_name()}'s coin landed on {result2}.")

    print(f"\Current Wallets:")
    print(f"{player1.get_name()}: ${player1.get_wallet()}")
    print(f"{player2.get_name()}: ${player2.get_wallet()}")
    
print("\nGame Over!")

if player1.get_wallet() == 0:
    print(f"\n{player2.get_name()} wins the game!")
else:
    print(f"\n{player1.get_name()} wins the game!")