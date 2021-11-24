
from game import Game

import random

options = ["rock", "paper", "scissor"]

player = input('What is your move? (rock, paper, scissor)\n: ')

pc = random.choices(options)[0]
print('Computer Move: ', pc)

game = Game()

result = game.play(player, pc)

print('The result of the game is: ', result)


