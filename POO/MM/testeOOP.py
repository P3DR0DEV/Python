class Animal:  #SuperClass
    def __init__(self, nome , idade):
        self.nome = nome
        self.idade = idade

    def show(self):
        print(f'I\'m {self.nome} and i have {self.idade} years old.')

    def speak(self):
        print('I don\'n Know what to say')
#   
#       
#{
class Dog(Animal): #SubClasses
    def __init__(self, nome, idade, color):
        super().__init__(nome, idade)
        self.color = color

    def speak(self):
        print('Bark!')
    
    def show(self):
        print(f'I\'m {self.nome} and i have {self.idade} years old and i\'m {self.color}.')

class Cat(Animal):  #SubClasses

    def speak(self):
        print('Meow!')

#}


animal = Animal('Pitoco', 6)
animal.show()
animal.speak()

dog = Dog('Duque', '0', 'Verde')
dog.show()
dog.speak()

cat = Cat('Maya', 7)
cat.show()
dog.speak()