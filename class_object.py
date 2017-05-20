### class_object.py
class Ball:
    def bounce(self):
        if self.direction == "down":
            self.direction = "up"
        elif self.direction == "up":
            self.direction = "down"

myBall = Ball()
myBall.color = 'red'
myBall.size = 'big'
myBall.direction = 'down'
print (myBall.color)
print (myBall.size)
print (myBall.direction)

print ('Call bounce method!')
myBall.bounce()
print (myBall.direction)

print ('Call bounce method!')
myBall.bounce()
print (myBall.direction)
