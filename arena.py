
'''
Author:      Anneliese Hall
Date:        4/7/26
Assignment:  Project 2 | Part 1 | Animon
Course:      CPSC 1050
Lab Section: 001
'''

# Module Imports 
from deck_empty_error import DeckEmptyError
import deck as d 
import trainer as t
import animon as a 

class Arena:
    """
    where the two trainers compete 
    """
    def __init__(self, trainer1, trainer2):
        """
        self.trainer  = supposed to call trainer() in main in diff object 
        self.battle_log = Just an empty list (going to hold strings)
        self.trainer_dd = also an empty list meant for stats later (going to hold ints)
        
        I know there are two versions of trainer ad dd but i dont want to be repetitave  
        """
        self.trainer1 = trainer1
        self.trainer2 = trainer2
        self.battle_log = []
        
        self.trainer1_dd = []
        self.trainer2_dd = []
        self.rounds_played = 1
        
    def play_round(self, round_num):
        """
        one whole round of the game 
        
        card1 and card2: what cards the players draw # ( 1 element of list holding the animon)
        damage_to_#: the damage that is done to player # (int)
        
        return -> Summarystring: the summary of the round (str)
        """
        
        # both players draw a creature draw card 
        card1 = self.trainer1.draw_card()
        card2 = self.trainer2.draw_card()

        # each creature calcualtes damage 
        damage_to_2 = card1.calculate_damage(card2)
        damage_to_1 = card2.calculate_damage(card1)

        # keep track of damage dealt 
        self.trainer1_dd.append(damage_to_2)
        self.trainer2_dd.append(damage_to_1)
        
        #damage applied to the opposing trainer
        self.trainer1.take_damage(damage_to_1)
        self.trainer2.take_damage(damage_to_2)

        # build a summary string and append it to battle log
        summarystring = f"Round {round_num}:\n  {self.trainer1.get_name()} sends out {card1}\n  {self.trainer2.get_name()} sends out {card2}\n  {card1.get_name()} deals {damage_to_2} damage to {self.trainer2.get_name()}\n  {card2.get_name()} deals {damage_to_1} damage to {self.trainer1.get_name()}\n  {self.trainer1.get_name()}: {self.trainer1.get_health()} HP | {self.trainer2.get_name()}: {self.trainer2.get_health()} HP"
        self.battle_log.append(summarystring)
        
        # return summary string 
        return summarystring
    
    def play_game(self):
        """
        Deck Empty Error Exception present
        
        round_num is initialized here as one to keep track of battles
        
        Decides who wins (if statements)
        - result appends to battle log because that is what we are using to print
        """
        
        # Try Block Start 
        try:
            
            while self.trainer1.is_alive() and self.trainer2.is_alive():
                self.play_round(self.rounds_played)
                self.rounds_played += 1
                
        # appends the error to the battle_log because thats how we print it out in the main
        except DeckEmptyError as e:
            self.battle_log.append(f"  {e}")
        
        # who wins decision 
        if self.trainer1.is_alive() == False:
            self.battle_log.append(f"  Trainer 2 wins!")
        elif self.trainer2.is_alive() == False:
            self.battle_log.append(f"  Trainer 1 wins!")
        else: 
            self.battle_log.append(f"  It's a draw!")
            
            
            

    def get_battle_log(self):
        """
        returns the battle_log str 
        """
        return self.battle_log

    def get_statistics(self):
        """
        returns the stats str
        """
        stats = f"=== Battle Statistics ===\n  Rounds played: {self.rounds_played -1 }\n  {self.trainer1.get_name()} total damage dealt: {sum(self.trainer1_dd)}\n  {self.trainer2.get_name()} total damage dealt: {sum(self.trainer2_dd)} "
        return stats 

    def save_log(self, filename):
        """
        creates battlelog_txt file 
        adds the battle log and the stats 
        returns the save statement 
        """
        # Creates battlelog.txt and saves the battles to it
        with open("battlelog.txt", 'w') as bl:
            
            # adds all the battles to the file
            for battle in self.battle_log:
                bl.write(battle +"\n")
                
            # adds the stats to the end of the file
            stats = self.get_statistics()
            bl.write(stats)
                
        return f"Battle log saved to {filename}"
    
