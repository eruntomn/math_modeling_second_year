class Ball:
    color = 'red'
    radius = 5

ball = Ball ()

print(ball.color)
print(ball.radius)

print(dir(ball)) #dir - команда, которая вызыывает все встроенные методы

print(dir(Ball))

print(ball.__init__())
print(Ball.__init__)