

class Game():
    def play(self, a, b):
        if a == 'rock' and b == 'scissor':
            return a
        elif a == 'rock' and b == 'paper':
            return b
        elif a == 'rock' and b == 'rock':
            return 'draw'
        
        elif a == 'paper' and b == 'rock':
            return a
        elif a == 'paper' and b == 'scissor':
            return b
        elif a == 'paper' and b == 'paper':
            return 'draw'

        elif a == 'scissor' and b == 'paper':
            return a
        elif a == 'scissor' and b == 'rock':
            return b
        elif a == 'scissor' and b == 'scissor':
            return 'draw'

        else:
            return 'error'
