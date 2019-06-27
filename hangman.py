# -*- coding: utf-8 -*-
"""
Created on Thu Jun 27 13:10:14 2019

@author: h_fur
"""

def hangman(word):
    wrong = 0
    stages = ["",
              "_____     ",
              "|         ",
              "|    |    ",
              "|    0    ",
              "|   /|\   ",
              "|   / \   ",
              "|         "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("Welcome to Hangman!")
    
    while wrong < len(stages) - 1:
        print("\n")
        msg = "Please pick a word: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
            print(" ".join(board))
            e = wrong + 1
            print("\n".join(stages[0:e]))
        if "_" not in board:
            print("You Win!")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong + 1]))
        print("You lose... The correct answer is {}.".format(word))

hangman("computer")