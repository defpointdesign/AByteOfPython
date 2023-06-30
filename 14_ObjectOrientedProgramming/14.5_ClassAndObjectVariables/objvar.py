class Robot:
    '''Represents a robot, with a name.'''

    # A class variable, counting the number of robots
    population = 0

    def __init__(self, name):
        '''Initializes the data'''
        self.name = name
        print('(Initializing {})'.format(self.name))
        # When this person is created, the robot adds to the population
        Robot.population +=1
    def __del__(self):
        '''I am dying'''
        print ('{} is being destroyed'.format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print('{0} was the last one.'.format(self.name))
        else:
            print('There are still {:d} robots working.'.format(Robot.population))

    def sayHi(self):
        '''Greating by the robot.
        Yeah, they can do that.'''
        print('Greetings, my masters call me {}.'.format(self.name) )

    def howMany():
        '''Prints the current population'''
        print('We have {:d} robots.'.format(Robot.population))
    howMany=staticmethod(howMany)

    @staticmethod
    def how_many():
        '''Print number of Robots'''
        print('We have {0:d} Robots.'.format(Robot.population))


droid1 = Robot('R2-D2')
droid1.sayHi()
Robot.howMany()

droid2 = Robot('C-3P0')
droid2.sayHi()
Robot.howMany()

print('\nRobot can do some work here.\n')
print("Robot have finished their work. So let's destroy them")

del droid1
del droid2
Robot.howMany()
Robot.how_many()
print(Robot.__doc__)
print(Robot.__del__.__doc__)
