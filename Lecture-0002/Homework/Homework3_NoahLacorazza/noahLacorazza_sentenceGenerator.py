# File: noahLacorazza_sentenceGenerator.py
# Author: Noah Lacorazza
# Date: 9/23/25
# Section: 1004
# E-mail: noah.lacorazza@maine.edu
# Description:
# Lets the user input a list of nouns, verbs, and adjectives, then builds 5 sentences using them
# Collaboration:
# N/A

nouns = input("Enter a list of 5 nouns separated by \", \": ").split(", ")
adjectives = input("Enter a list of 5 adjectives separated by \", \": ").split(", ")
verbs = input("Enter a list of 5 verbs separated by \", \": ").split(", ")

print(f"""Nouns: {nouns}
Adjectives: {adjectives}
Verbs: {verbs}""")

base_word = input("Enter a one word sentence. Ex \"The\": ")

for i in range(5):
    print(f"{base_word} {adjectives[i]} {nouns[i]} {verbs[i]}.")