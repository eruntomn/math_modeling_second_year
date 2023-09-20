class Ball ():
    #Динамические атрибуты класса(методы)
    # Методы, реализующие поведение экземпляров
    #self - подразумеваемый экземпляр
    def drop(self):
        print('Меня подкинули')
    
    def kick(self):
        print('Меня пнули')
        self.drop()

    def fail(self):
        print('Прокололся')
    
    def version(cls):
        print('Версия мяча 1:0')
    
ball = Ball ()

ball.drop()
ball.kick()
ball.fail()
ball.version()

Ball.version(ball)

