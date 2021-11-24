

from unittest import TestCase, result
from game import Game

class TestGame(TestCase):

    def setUp(self):
        self.game = Game()
    
    def tearDown(self):
        self.game = None

 
    def test_rock_win_scissor(self):
        a = 'rock'
        b = 'scissor'
        result = self.game.play(a, b)
        self.assertEqual(result, a)

        a = 'rock'
        b = 'paper'
        result = self.game.play(a, b)
        self.assertEqual(result, b)

    def test_paper_win_rock(self):
        a = 'paper'
        b = 'rock'
        result = self.game.play(a, b)
        self.assertEqual(result, a)

        a = 'paper'
        b = 'scissor'
        result = self.game.play(a, b)
        self.assertEqual(result, b)
        
    def test_scissor_win_paper(self):
        a = 'scissor'
        b = 'paper'
        result = self.game.play(a, b)
        self.assertEqual(result, a)

        a = 'scissor'
        b = 'rock'
        result = self.game.play(a, b)
        self.assertEqual(result, b)
  
    def test_invalid_play(self):
        a = 'xuxa'
        b = 'pelé' 
        result = self.game.play(a, b)
        self.assertEqual(result, 'error')
    
    def test_draw(self):
        a = 'rock'
        b = 'rock'
        result = self.game.play(a, b)
        self.assertEqual(result, 'draw')

        a = 'paper'
        b = 'paper'
        result = self.game.play(a, b)
        self.assertEqual(result, 'draw')

        a = 'scissor'
        b = 'scissor'
        result = self.game.play(a, b)
        self.assertEqual(result, 'draw')