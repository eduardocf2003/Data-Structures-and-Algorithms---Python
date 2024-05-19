class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self, color):
        self.color = color


cookie_one = Cookie('blue')
cookie_two = Cookie('purple')

print(cookie_one.get_color())
print(cookie_two.get_color())

cookie_two.set_color('yellow')

print(cookie_two.get_color())

#Uma classe é basicamente uma forma de criarmos nosso próprio tipo de dados, por exemplo, nesse código criamos 
#o tipo de dado cookie, que tem como atributo sua cor (color).