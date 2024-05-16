#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 09:34:08 2024

@author: justinesilverstein
"""

#SilversteinJ25

# Create a rock-paper-scissors game!
# - Play once and report the result
# - Play in a loop and record how many wins and losses happen?
# - Allow choosing how many human players there are, from 0-2?
# - Organize everything into functions?
# - Organize everything into classes??

from numpy import random

# using globals
choices = ['rock', 'paper', 'scissors']
beats = {'rock':'scissors',
        'scissors':'paper',
        'paper':'rock'}

p1 = input('Pick one of rock, paper or scissors: ')
p2 = random.choice(choices)

if beats[p1]== p2:
    print('p1 wins!')
elif beats[p2] == p1:
    print('p2 wins!')
else:
    print('tie')


#functions
def game(p1):
    if p1 == 'rock':
        statement = 'rock'
    elif p1 == 'scissors':
        statement = 'scissors'
    elif p1 == 'paper':
        statement = 'paper'
    else:
        statement = 'play again!'
    

#using functions
choices = ['rock', 'paper', 'scissors']
beats = {'rock':'scissors',
         'scissors':'paper',
         'paper':'rock'} 
    
def find_winner (p1,p2):
    if beats[p1] == p2:
        return 'player one wins'
    elif beats[p2]== p1:
        return 'player 2 wins'
    else:
        return 'tie'
    
def readysetgo():
    return random.choice(choices)
    
def play_once():
    p1 = readysetgo()
    p2 = readysetgo()
    print(f'p1: {p1}\np2: {p2}')
    
    winner = find_winner(p1, p2)
    print(f'the winner is: {winner}')

# using classes    
























