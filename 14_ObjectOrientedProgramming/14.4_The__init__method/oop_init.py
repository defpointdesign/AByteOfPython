class Person:
    def __init__(self, name):
        self.name = name

    def say_hi(self):
        print('Hi, my name is,', self.name)

p=Person('Jo')
p.say_hi()
