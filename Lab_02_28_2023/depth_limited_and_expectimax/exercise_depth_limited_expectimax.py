# -*- coding: utf-8 -*-
"""Exercise_Depth_Limited_Expectimax.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1EYvwMud0RLcxv6vLPWVzU28UcTPpUivv

##Depth limited search - Pseudocode

```
function depth_limited_expectimax(node, depth):
    if depth == 0 or node is a terminal node:
        return the node's score

    if node is a max node:
        best_score = -infinity
        for each child of node:
            score = depth_limited_expectimax(child, depth - 1)
            best_score = max(best_score, score)
        return best_score

    if node is an expect node:
        avg_score = 0
        num_children = 0
        for each child of node:
            score = depth_limited_expectimax(child, depth - 1)
            avg_score += score
            num_children += 1
        return avg_score / num_children

```
"""

import random

class RollTheDice:
    def __init__(self):
        self.player_score = 0
        self.opponent_score = 0
        self.turn = 'player'

    def is_game_over(self):
        return self.player_score >= 25 or self.opponent_score >= 25

    def evaluate(self):
        return self.player_score - self.opponent_score

    def get_possible_actions(self):
        return ['roll']

    def apply_action(self, action):
        if action == 'roll':
            if self.turn == 'player':
                self.player_score += random.randint(1, 6)
                self.turn = 'opponent'
            else:
                self.opponent_score += random.randint(1, 6)
                self.turn = 'player'
        return self

def expectimax(state, depth, player):
    if state.is_game_over() or depth == 0:
        return state.evaluate(), None

    if player == 'player':
      #ENTER CODE FOR MAXIMIZING PLAYER
      pass

    else:
      #ENTER CODE HERE FOR CHANCE PLAYER
      pass


game = RollTheDice()
while not game.is_game_over():
    if game.turn == 'player':
        print("Your score:", game.player_score)
        print("Opponent score:", game.opponent_score)
        action = input("Roll? ")
    else:
        _, action = expectimax(game, depth=3, player='opponent')
        print("Opponent rolled.")
    game.apply_action(action)

if game.player_score >= 25:
    print("You win!")
else:
    print("You lose.")