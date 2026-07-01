'''
Author:      Anneliese Hall
Date:        4/7/26
Assignment:  Project 2 | Part 1 | Animon
Course:      CPSC 1050
Lab Section: 001
'''

class DeckFullError(Exception):
    """
    A custom exception raised when a trainer tries to add a card to a deck that is at maximum capacity.
    """

    def __init__(self, e_name, d_maxsize):
        """
        Initializes...
        
        self.name = str, deck's owner 
        
        self.maxsize = int, max size of the deck 
        """
        
        self.name = e_name 
        self.maxsize = d_maxsize
    

    def __str__(self):
        """
        return = string representation of deck full error
        """
        return f"{self.name}'s deck is full! (max {self.maxsize} cards)"
        

