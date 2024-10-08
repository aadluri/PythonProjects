import random

class Die:
    ''' A class to represent one 'die'. Takes
    '''
    def __init__(self):
        '''Function to initialize a die, set current value to zero, set max value'''
        self.__value = 0
        self.__max = 7

    @property
    def value(self):
        '''Function to return value of die given a value, invoked internally'''
        return self.__value
                
    @value.setter
    def value(self, value):
        '''function to assign value, invoked internally'''
        self.__value = value
                
    def roll(self):
        '''sets die to a ramdon value between 1 and given maximum from :func:`~MyClass.__init__`, invoked internally by Dice'''
        self.__value = random.randrange(1, self.__max)

                
class Dice:
    def __init__(self):
        '''Internal function to initialize list of values'''
        self.__list = []

    def addDie(self, die):
        '''Function to add a die to list of dice '''
        self.__list.append(die)

    @property
    def list(self):
        '''Internal function to return dice value - loop through to list all dice. Returns a tuple'''
        dice_tuple = tuple(self.__list)
        return dice_tuple
                
    def rollAll(self):
        ''' Function to roll all dice in list self.__list, returns values from randomizer '''
        for die in self.__list:
            die.roll()
