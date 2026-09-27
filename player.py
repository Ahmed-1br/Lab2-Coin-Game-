"""
Program Name: Match Coins Game - Player Class
Author: Ahmed Ibrahim
Purpose: Defines the Player class used to represent a player in the coin tossing game.
Starter Code: None
Date: September 27, 2026
"""

from coin import Coin

class Player:
    def __init__(self, name):
        self.__coin = Coin()
        self.__name = name
        self.__wallet = 20

    def toss_coin(self):
        self.__coin.toss()

    def get_coin_side(self):
        return self.__coin.get_side_up()

    def win_coin(self):
        self.__wallet += 1

    def lose_coin(self):
        self.__wallet -= 1

    def get_wallet(self):
        return self.__wallet

    def get_name(self):
        return self.__name