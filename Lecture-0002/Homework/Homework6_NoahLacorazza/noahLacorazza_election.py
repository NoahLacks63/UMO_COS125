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

candidates = {}

def main():
    used_numbers = set()

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
        used_nums = set()

        first_choice = candidate_names[unique_int(used_nums, 0, 4)]

        candidates[first_choice].append({
            "ID" : unique_int(used_numbers, 0, 1000000),
            1 : first_choice,
            2 : candidate_names[rank_candidates(used_nums)],
            3 : candidate_names[rank_candidates(used_nums)],
            4 : candidate_names[rank_candidates(used_nums)],
            5 : candidate_names[rank_candidates(used_nums)]
        })
    
    
    

def unique_int(used_numbers, min, max):
    num = random.randint(min, max)

    while num in used_numbers:
        num = random.randint(min, max)

    used_numbers.add(num)

    return num


def vote_round():
    loser = list(candidates.keys()[0])

    for key, value in candidates:
        if candidates[loser] <= value:
            loser = key
    
    for voter in candidates[loser]:
        voter.pop(voter.keys()[1])

        candidates[voter.keys()[1]].append(voter)
    
    candidates.pop(loser)

def rank_candidates(used_nums):
    return unique_int(used_nums, 0, 4)

main()