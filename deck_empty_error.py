'''
Author:      Anneliese Hall
Date:        4/7/26
Assignment:  Project 2 | Part 1 | Animon
Course:      CPSC 1050
Lab Section: 001
'''


class DeckEmptyError(Exception):
    """
    checks to see if the deck is empty or not 
    """
    
    def __init__(self, name):
        """
        initalizes...
         
           - self.name    :  
           - self.maxsize :
        """ 
        
        self.name = name 

    def __str__(self):
        """
        returns the string format of the class. what prints out when we raise the execption as lol and print(lol)
        """
        return f"{self.name}'s deck is empty!"

