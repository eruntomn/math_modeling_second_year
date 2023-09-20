class Ball:
    #Создание статических атрибутов класса
    color = 'red'
    radius = 5

    #Статический метод
    def info():
        print('Просто хороший класс')

ball = Ball ()

#Вызов статических атрибутов
print(ball.color)
#print(ball.info()) ERROR
print(Ball.radius)
Ball.info()

ball.color = 'white'
print(ball.color)
print(Ball.color)

Ball.color = 'white'
new_ball = Ball ()
print(new_ball.color)