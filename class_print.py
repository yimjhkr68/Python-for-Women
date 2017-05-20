### class_print.py
class Ball:
    def __init__(self, color, size, direction):
        self.color = color
        self.size = size
        self.direction = direction
    def __str__(self):
        return "Hi, I'm a " + self.size + " " + self.color + " ball~"

myBall = Ball('red', 'big', 'down')
print (myBall)
