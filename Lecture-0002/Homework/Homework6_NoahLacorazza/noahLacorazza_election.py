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
    candidates = build_ballot()[0]
    num_candidates = build_ballot()[1]



def build_ballot():
    candidates = {}
    num_candidates = int(input("Enter number of candidates (greater than 3): "))

    while num_candidates < 3:
        num_candidates = int(input("Enter number of candidates (greater than 3): "))

    for n in range(1, num_candidates + 1):
        candidates[input(f"Enter candidate {n}'s name: ")] = []
    
    return [candidates, num_candidates]

def build_electorate(num_candidates):

    electorate = []

    for n in range(input("")):
