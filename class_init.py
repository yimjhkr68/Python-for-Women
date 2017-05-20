### class_init.py
class Ball:
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction
    def bounce(self):
        if self.direction == 'down':
            self.direction = 'up'
        elif self.direction == 'up':
            self.direction = 'down'


myBall = Ball('red', 'big', 'down')
print (myBall.__dict__)

myBall.bounce()
print (myBall.__dict__)
