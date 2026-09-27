"""
Program Name: Match Coins Game - Coin Class
Author: Ahmed Ibrahim
Purpose: Defines the Coin class used to represent and toss a coin.
Starter Code: None
Date: September 27, 2026
"""

import random

class Coin:
    def __init__(self):
        self.__sideup = "Heads"

    def toss(self):
        if random.randint(0, 1) == 0:
            self.__sideup = "Heads"
        else:
            self.__sideup = "Tails"

    def get_side_up(self):
        return self.__sideup