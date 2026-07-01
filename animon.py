'''
Author:      Anneliese Hall
Date:        4/7/26
Assignment:  Project 2 | Part 1 | Animon
Course:      CPSC 1050
Lab Section: 001
'''

from invalid_stat_error import InvalidStatError
from deck_full_error import DeckFullError

class Animon:
    """Base class for all Animon creatures.

    The getters, calculate_damage, and __str__ are fully implemented.
    You need to implement __eq__ and the three subclasses below.
    """

    def __init__(self, name, power, defense):
        self.name = name
        self.animon_type = "Normal"
        
        
        # Try/Except for power!
        try:
            self.power = power
            
            if power < 0:
                raise InvalidStatError(stat_name ="power", stat_value = power)
            
        except InvalidStatError as lol:
            print(lol)
            raise 

            
        # Try/Except for defense!
        try:
            self.defense = defense 
            if defense < 0:
                raise InvalidStatError(stat_name ="defense", stat_value = defense)
            
        except InvalidStatError as lol:
            print(lol)
            raise 




    def get_name(self):
        return self.name

    def get_power(self):
        return self.power

    def get_defense(self):
        return self.defense

    def get_animon_type(self):
        return self.animon_type

    def calculate_damage(self, opponent):
        return max(0, self.power - opponent.get_defense())
    

    def __eq__(self, other):
        """
        __eq__ -> allows for statements like: if animon1 == animon2 ... 
        
        under tha hood:
        1. checks if self.attribute is equal to other.getterattribute 
        2. returns true if equal
        3. returns false if not equal 
        
        ez 
        """
        
        # My current understanding:
        # if a water animon and normal animon try to compare, 
        # this is what occurs 
        if not isinstance(other, Animon):
            return False
        
        if other.get_animon_type() != self.animon_type:
            return NotImplemented # tells python the comparison does not appply
        
        if (other.get_animon_type() == self.animon_type) and (other.get_name() == self.name) and (other.get_power() == self.power) and (other.get_defense() == self.defense):
            return True 
            


    def __str__(self):
        return f"[{self.animon_type}] {self.name} (Power: {self.power}, Defense: {self.defense})"







class FireAnimon(Animon):
    """
    FireAnimon(Animon) -> a child class that inherits parent, Animon
    
    """
    def __init__(self, name, power, defense):
        """
        super().__init__ -> just calls all the methods from the parent class
        
        initializes instance attribute animon_type and sets it to "Fire"
        """    
    
        super().__init__(name, power, defense) 
        self.animon_type = "Fire" # only thing different from base class
        
        
        
        
    # I'm realizing now I could have made these wayyyy less redundant, sorry to whoever is grading
    def calculate_damage(self, opponent):
        """
        returns -> the final result, real_result, in int form dependant on opponent animon type
            
        get_animon_type -> MUST BE CALLED TO FIND THE OPPONENT ANIMON TYPE (idk if you can tell but i tripped up on this)
            
        in fact all getters must be called when finding attributes for opponents 
            
        """
        
        # Grass Damage Calc
        if opponent.get_animon_type() == "Grass": 
            result = max(0, self.power - opponent.get_defense()) * 1.5 # apply multiplier 
            real_result = int(result) # turns into Int
            return real_result 
        
         # Water Damage Calc
        if opponent.get_animon_type() == "Water":
            result = max(0, self.power - opponent.get_defense()) * 0.5 # apply multiplier
            real_result = int(result) # turns into Int 
            return real_result
        
         # Fire Damage Calc
        if (opponent.get_animon_type() == "Fire") or (opponent.get_animon_type() == "Normal"): 
            result = max(0, self.power - opponent.get_defense()) * 1
            real_result = int(result)
            return real_result



class WaterAnimon(Animon):
    """
    same exact structure as fire animon 
    """
    
    def __init__(self, name, power, defense):
        """
        super().__init__ -> just calls all the methods from the parent class
                
        initializes instance attribute animon_type and sets it to "Water"
        """    
        
        super().__init__(name, power, defense)
        self.animon_type = "Water"


    def calculate_damage(self, opponent):
        """
        returns -> the final result, real_result, in int form dependant on opponent animon type
                
        get_animon_type -> MUST BE CALLED TO FIND THE OPPONENT ANIMON TYPE (idk if you can tell but i tripped up on this)
                
        in fact all getters must be called when finding attributes for opponents 
                
        """
        if opponent.get_animon_type() == "Grass":
            result = max(0, self.power - opponent.get_defense()) * 0.5
            real_result = int(result)
            return real_result
        
        if (opponent.get_animon_type() == "Water") or (opponent.get_animon_type() == "Normal"):
            result = max(0, self.power - opponent.get_defense()) 
            real_result = int(result)
            return max(0, self.power - opponent.get_defense())
          
        if opponent.get_animon_type() == "Fire":  
            result = max(0, self.power - opponent.get_defense()) * 1.5
            real_result = int(result)
            return real_result




class GrassAnimon(Animon):
    """
    same exact structure as fire and water animon
    """

    def __init__(self, name, power, defense):
        """
        super().__init__ -> just calls all the methods from the parent class
                
        initializes instance attribute animon_type and sets it to "Grass"
        """ 
        
        super().__init__(name, power, defense)
        self.animon_type = "Grass"

    def calculate_damage(self, opponent):
        """
        returns -> the final result, real_result, in int form dependant on opponent animon type
            
        get_animon_type -> MUST BE CALLED TO FIND THE OPPONENT ANIMON TYPE (idk if you can tell but i tripped up on this)
            
        in fact all getters must be called when finding attributes for opponents 
            
        """
        
        if (opponent.get_animon_type() == "Grass") or (opponent.get_animon_type() == "Normal"):
            result = max(0, self.power - opponent.get_defense())
            real_result = int(result)
            return real_result
        
        if opponent.get_animon_type() == "Water":
            result = max(0, self.power - opponent.get_defense()) * 1.5
            real_result = int(result)
            return real_result
          
        if opponent.get_animon_type() == "Fire": 
            result = max(0, self.power - opponent.get_defense()) * 0.5
            real_result = int(result)
            return real_result
 
