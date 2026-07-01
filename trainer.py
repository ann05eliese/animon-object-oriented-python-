'''
Author:      Anneliese Hall
Date:        4/7/26
Assignment:  Project 2 | Part 1 | Animon
Course:      CPSC 1050
Lab Section: 001
'''

# Import proper files 
from deck import Deck


class Trainer:
    """
    """

    def __init__(self, name, health_points):
        """
        initializes...
        self.name = the name of trainer
        self.health_points = the subjective health points
        self.initial_health = the max health points 
        self.deck = Deck() (instantiating the class we imported )
        """
        
        self.name = name 
        self.health_points = health_points
        self.initial_health = health_points
        self.deck = Deck(owner_name=name)
        
    def get_name(self):
        """
        getter!
        
        returns the name of the trainer
        """
        return self.name

    def get_health(self):
        """
        getter!
        
        returns the subjective health points 
        """
        return self.health_points

    def is_alive(self):
        """
        Bool :)
        
        self.health_points = int 
        
        returns true or false depending on comparison
        """
        
        if self.health_points > 0:
            return True
        else:
            return False 

    def take_damage(self, amount):
        """
        max() funciton used to pick the largest integer out of the two.
        so if zero is the biggest int, the self.health_points will be zero
        
        self.health_points = the health points subject to change
        amount = amount to be healed 
        
        """
        
        self.health_points = max(0, self.health_points - amount)
        

    def heal(self, amount):
        """
        min used to make sure the value doesnt rise above the intial health
        
        self.health_points = the health points subject to change
        self.intial_health = the max health of the animon 
        amount = amount to be healed 
        
        """
        # Calculating restored health

        self.health_points = min(self.initial_health, self.health_points + amount)

    def add_card_to_deck(self, card):
        """
        adds card to this trainer's deck 
        composition -> self.deck.add_card
        
        "card = card" is very important, the assignment is needed to work for the program to run correctly
        
        return -> card added to deck  
        """
        return self.deck.add_card(card = card)

    def shuffle_deck(self):
        """
        randomizes the deck belongning to this trainer 
        self.deck.shuffle() -> composition
        """
        return self.deck.shuffle()

    def draw_card(self):
        """
        returns the card drawn for the specific deck of the trainer 
        self.deck.draw_card() -> composition
        """
        return self.deck.draw_card()

    def __str__(self):
        """
        string representation of the class Trainer 
        uses...
        
        self.name            -> Attribute of Trainer (the name)
        self.health_points   -> Attribute of Trainer (the healthpoints subject to change )
        self.deck.size()     -> Composition
        """
        return f"{self.name} (HP: {self.health_points}, Deck: {self.deck.size()} cards)"
