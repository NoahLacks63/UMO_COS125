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

        first_choice = candidate_names[rank_candidates(used_nums) - 1]

        candidates[first_choice].append({
            "ID" : unique_int(used_numbers, 0, 1000000),
            1 : first_choice,
            2 : candidate_names[rank_candidates(used_nums)],
            3 : candidate_names[rank_candidates(used_nums)],
            4 : candidate_names[rank_candidates(used_nums)],
            5 : candidate_names[rank_candidates(used_nums)]
        })
    
    round = 1
    winner = None
    while winner == None:
        print_round(candidates, round)

        for candidate, voters in candidates.items():
            if len(voters) > num_voters / 2:
                winner = candidate
        
        round += 1
        
        if winner == None:
            vote_round(candidates)

def unique_int(used_numbers, min, max):
    num = random.randint(min, max)

    while num in used_numbers:
        num = random.randint(min, max)

    used_numbers.add(num)

    return num


def vote_round(candidates):
    loser = list(candidates.keys())[0]

    for key, value in candidates.items():
        if len(candidates[loser]) >= len(value):
            loser = key
    
    for voter in candidates[loser]:
        voter.pop(list(voter.keys())[1])

        next_rank = voter[list(voter.keys())[1]]

        sentinal = True
        while sentinal:
            for candidate in candidates.keys():
                if next_rank == candidate:
                    sentinal = False
            
            if sentinal:
                voter.pop(list(voter.keys())[1])
                next_rank = voter[list(voter.keys())[1]]

        candidates[next_rank].append(voter)
    
    candidates.pop(loser)
    print(f"Loser: {loser}")

def rank_candidates(used_nums):
    return unique_int(used_nums, 0, 4)

def print_round(candidates, round):
    print(f"\nRound: {round}")
    print("--------------------")

    for candidate, voters in candidates.items():
        print(f"{candidate:5} | {len(voters)}")

main()