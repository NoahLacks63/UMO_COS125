# File: noahLacorazza_dice.py
# Author: Noah Lacorazza
# Date: 10/20/25
# Section: 1004
# E-mail: noah.lacorazza@maine.edu
# Description:
# Rolls 50 dice. Determines the frequency that each number shows up, then assigns point values to each number.
# The user then plays a game where they choose a number of die to roll. If their total is divisible by 7 
# evenly, they win
# Collaboration:
# N/A

import random

points = {}

def main():
    """
    Finds point values based on the frequency of 50 dice rolls using the find_points method.
    """
    # a dictionary made to hold the frequency each number on a die is rolled
    dice = {
        1 : 0,
        2 : 0,
        3 : 0,
        4 : 0,
        5 : 0,
        6 : 0
    }

    # rolls 50 dice and tracks their frequency
    for i in range(50):
        dice[roll(1)[0]] += 1
    
    points = find_points(dice)

    print_dict(dice, "Dice Rolls")
    print_dict(points, "Point Values")

    game()

def game():
    """
    Rolls a user-specified number of dice. Each number is multiplied by its 
    frequency based on 50 rolls done earlier. You win if your score is divisible by 7.
    The game can be infinitely repeated using the same point values.
    """
    score = 0
    num_dice = int(input("How many dice would you like to play with?: "))

    hand = roll(num_dice)

    # Calculates score based on hand
    for die in hand:
        score += points[die]

    print(f"Your score: {score}")

    # Finds if score is divisible by 7
    if score % 7 == 0:
        print("You win! :D")
    else:
        print("You lose! D:")

    # Asks if you'd like to play again
    if input("Would you like to play again? y/n: ") == "y":
        game()


def roll(rolls):
    """
    Rolls multiple dice based on the rolls variable using the roll() function.

    Args:
        rolls (int): The number of die to be rolled
    
    Returns:
        list (int): A list of die rolls
    """
    hand = []

    for i in range(rolls):
        hand.append(random.randint(1, 6))
    
    return hand

def find_points(dice):
    """
    Finds the multiplier for each number based on frequency of the 50 rolls.

    Returns:
        dict (int, int): A dictionary that gives point values to each die face.
    """
    points = {}
    sorted_dice = sorted(dice, key=dice.get)

    i = 1
    for key in sorted_dice:
        points[key] = i * key
        i += 1
    
    return points

def print_dict(dictionary, title):
    """
    Prints out a dictionary in a pleasent looking way.

    Args:
        dictionary (dict): The dictionary to be printed out.
        title (str): The title of what the dictionary represents.
    """
    keys = list(dictionary.keys())
    values = list(dictionary.values())

    print(title)
    print("--------------------")

    for i in range(len(dictionary)):
        print(f"{keys[i]:5} | {values[i]}")

main()