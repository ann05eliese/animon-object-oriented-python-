'''
Author:      Anneliese Hall
Date:        4/7/26
Assignment:  Project 2 | Part 1 | Animon
Course:      CPSC 1050
Lab Section: 001
'''


class InvalidStatError(Exception):
    """
    A custom exception raised when an Animon is created with an invalid (negative) stat.
    """
    

    def __init__(self, stat_name, stat_value):
        """
        Initializes... 
         
         self.stat_name = string, could be applied to "defense" or "power"
         
         self.stat_value = the value of defense or power
        """
        
        self.stat_name = stat_name
        self.stat_value = stat_value

    def __str__(self):
        """
        string represetnation of the error that pops up when called 
        """
        
        return f"Invalid {self.stat_name}: {self.stat_value} (must be non-negative)"
