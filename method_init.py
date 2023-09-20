class Ball:

    def __init__(self, mass): #self - на первом месте
        ''' Инициализатор (конструктор) — это
            специальный метод, который вызывается по
            умолчанию когда вы создаете экземпляр класса.
        '''
        print('Я вызвался')

        self.mass = mass
        self.image = 'hexagone'
        self.x = 0
        self.y = 0
        self.state=True

    # Методы, реализующие поведение экземпляров
    # self – подразумеваемый экземпляр
    def drop(self):
        if self.state:
            print('Я подбросился')
            self.x += 2
        else:
            print('Я проколот, чувак')

    def kick(self):
        if self.state:
            print('Я пнулся')
            self.x += 1
        else:
            print('Я проколот, чувак')
        

    def fail(self):
        self.state = False
        self.mass = self.mass - 0.1

# Вызов полей
#print(Ball.color) # нельзя вызывать
#print(Ball.image)

ball = Ball(0.5) # аргументы доллжны быть ка и в функции
print(ball.image) #вызывает изображение 
print(ball.mass)

ball.image = 'lines'#перезапись
print(ball.image)

print(ball.x)
ball.drop() #вызов метиодов класса
print(ball.x)

ball.kick()

ball.fail()

print(ball.x)