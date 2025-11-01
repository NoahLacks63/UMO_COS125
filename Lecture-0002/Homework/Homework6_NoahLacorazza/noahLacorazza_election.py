# File: noahLacorazza_election.py
# Author: Noah Lacorazza
# Date: 10/27/25
# Section: 1004
# E-mail: noah.lacorazza@maine.edu
# Description:
# 
# Collaboration:
# N/A

import random

def main():
    """
    Initializes our candidates, voters, and calculates who is ranked first the most.
    """
    used_numbers = list()

    candidates = {
        input("Enter candidate one's name: "): [],
        input("Enter candidate two's name: "): [],
        input("Enter candidate three's name: "): [],
        input("Enter candidate four's name: "): [],
        input("Enter candidate five's name: "): []
    }

    candidate_names = list(candidates.keys())
    
    num_voters = int(input("Enter number of voters: "))

    for i in range(num_voters):
        used_nums = list()

        first_choice = candidate_names[rank_candidates(used_nums) - 1]

        candidates[first_choice].append({
            "ID" : unique_int(used_numbers, 0, 1000000),
            1 : first_choice,
            2 : candidate_names[rank_candidates(used_nums)],
            3 : candidate_names[rank_candidates(used_nums)],
            4 : candidate_names[rank_candidates(used_nums)],
            5 : candidate_names[rank_candidates(used_nums)]
        })

    winner = list(candidates.keys())[0]
    for candidate in candidates.keys():
        if len(candidates[winner]) < len(candidates[candidate]):
            winner = candidate
    
    print(f"Winner: {winner}")

def unique_int(used_numbers, min, max):
    """
    Provides a random int that is not listed in used_numbers.

    Args:
        used_numbers (list): A list of numbers that have already been used.
        min (int): The minimum random int.
        max (int): The maximum random int.
    """
    num = random.randint(min, max)

    while num in used_numbers:
        num = random.randint(min, max)

    used_numbers.append(num)

    return num

def rank_candidates(used_nums):
    return unique_int(used_nums, 0, 4)

main()