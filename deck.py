
'''
Author:      Anneliese Hall
Date:        4/7/26
Assignment:  Project 2 | Part 1 | Animon
Course:      CPSC 1050
Lab Section: 001
'''

import random
from deck_full_error import DeckFullError
from deck_empty_error import DeckEmptyError


class Deck:
    """
    contains various instance methods to 
    - initalize instance methods 
    - add a card to deck 
    - draw and remove card from deck 
    - peek at a card 
    - shuffle the deck 
    - get the size of deck 
    
    - __iter__       | all                  E
    -__len__         |     to               A
    -__str__         |        make          S
    -__contains__    |             coding   Y
   
    """    
    def __init__(self, owner_name ="Trainer", max_size = 10): 
        """
        owner name = str
        
        max_size = int
        
        self.cards_ = list 
        
        initializes instance attributes 
        """ 
        
        self.owner_name = owner_name         # initialized owner name 1/ default value  
        self.maxsize = max_size               # initialized max size w/ default value     
        self.cards_ = []                       # empty list initialized                   
        
        
        
        
        
        

    
    def add_card(self, card):                 #      *** Instance Method **** 
        """
        Comparison used to verify Max size is not exceeded
        
        len() -> used to count elements,cards, enabled by ___len___ method a few instances down
        
        append() -> used to add element, card to the list, deck 
        
        return -> the deck with the added card 
        """
        
        # Try Block Added 
        try:
            self.cards_.append(card)            # Adds the card to the list (deck)
            
            if len(self.cards_) > self.maxsize:
                raise DeckFullError(e_name = self.owner_name, d_maxsize = self.maxsize) #assignment necessary to work
            
        except DeckFullError as lol:
            self.cards_.pop()
            print(lol)
            raise 
        
        # what happens when error is not caught 
        return self.cards_                  # Returns the list  w/ added element (card)







    def draw_card(self):                       #** Instance Method ** 
        """
        pop() -> used to remove the first element, card, from list, deck 
        
        return -> the first card from the deck 
        
        first_card -> stores the first card drawn so i can return and pop it. 
        
        len() -> used to count elements, enabled by ___len___ method a few instances down
        """
        #checks for nonetype error in main.py that kept annoying the crap out of me 
        if len(self.cards_) == 0:
            raise DeckEmptyError(name = self.owner_name)
        
        first_card = self.cards_[0]          # stores 1st in list 
        self.cards_.pop(0)
        return first_card
            
            
        






    def peek(self):      
        """ 
        return -> first element of list, deck. 
        """     
        if len(self.cards_) == 0:
            raise DeckEmptyError(name = self.owner_name)               
        return self.cards_[0]   # index [0] of list, deck 
    
    
    
    
    

    def size(self):
        """
        return -> number of elements, cards, in deck 
        
        len() -> used to count elements, enabled by ___len___ method a few instances down
        
        """
        return len(self.cards_)
    
    
    
    

    def shuffle(self):
        """
        module, random, imported at the top
        
        shuffle -> random modules's function 
        
        shuffles the elements, cards, in list, deck  
        
        return -> returns the deck with its elements in a new order 
        """
        random.shuffle(self.cards_)






    def __len__(self):
        """
        len() -> used to count elements, enabled by ___len___ method a few instances down
        
        enables the len() to be used in other instance attributes to make life easy 
        """
        return len(self.cards_)

    
    
    
    def __iter__(self):
        """
        iter method - enables self.cards_s iteration, for loops and iter() wont work without it 
        
        iter() ->  required for __iter__ to work, opens self.cards_ up for iteration basically
        """
        return iter(self.cards_)





    def __contains__(self, card):
        """
        return -> each element, card, in list, deck 
        
        __contains__ -> checks each element in list and marks it as true or false (RETURN TO THIS WHEN WE CHECK CSV FILES)
            
            1. in method, returns true for card in self.cards_ 
            2. "card in list" in list | output = True
            3. "card not in list" in list | output = False 
        """
        return card in self.cards_






    def __str__(self):
        """
        __str__ represents the class as a string so we can do this:
        1. class_obj = class()
        2. print(class_obj)
        3. output -> whatever we returned in the __str__ method of the class 
        
        """
        plz_work = f"Deck:\n"
        for card in self.cards_:
            plz_work += f"  {card}\n"
        return plz_work