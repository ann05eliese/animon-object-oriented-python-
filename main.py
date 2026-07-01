
'''
Author:      Anneliese Hall
Date:        4/7/26
Assignment:  Project 2 | Part 1 | Animon
Course:      CPSC 1050
Lab Section: 001
'''

# import modules
import random
import sys
from animon import Animon, FireAnimon, WaterAnimon, GrassAnimon
from trainer import Trainer
from arena import Arena
from deck import Deck



def load_animon(file_):
    """
    Loads animon files 
    
    several "with" statements to open and read the files 
    try1 = a converted file to 2dlist of str name, type, power, defense
    
    isdigit() used to convert defense and power into useable ints
    
    returns a fully functional animon deck 
    """
    # empty list to store all the loaded animon once converted 
    animon_list = []
    
    # opens deck, strips, and splits the deck
    with open(file_, 'r') as decks:
        decks.readline()
        try1 = [line.strip().split(",") for line in decks]
    
    # turns the number strings into int values 
    for i in range(len(try1)):
        for j in range(len(try1[i])):
            
            if try1[i][j].isdigit():
                try1[i][j] = int(try1[i][j])
    
    # converts each item in the list into their animon types 
    for i in range(len(try1)):   
        if try1[i][1] == 'Grass':
            animon_list.append(GrassAnimon(try1[i][0], try1[i][2], try1[i][3]))
        elif try1[i][1] == 'Fire':
            animon_list.append(FireAnimon(try1[i][0], try1[i][2], try1[i][3]))
        elif try1[i][1] == 'Water':
            animon_list.append(WaterAnimon(try1[i][0], try1[i][2], try1[i][3]))
        elif try1[i][1] == 'Normal':
            animon_list.append(Animon(try1[i][0], try1[i][2], try1[i][3]))
                    
    return animon_list

if __name__ == "__main__":
    random.seed(42)

    print("=== Animon Battle Arena ===")
    print("  Gotta Battle 'Em All!(tm)")
    print()
    # Logic for this is not the issue? no change in grade 
    # no command, default to one of the two files
    if len(sys.argv) == 1: 
        deck_one = 'deck1.csv'
        deck_two = 'deck2.csv'
        
    # checks command line for specific deck1, default deck2.csv
    if len(sys.argv) == 2:
        deck_one = sys.argv[1]
        deck_two = 'deck2.csv'
        
    # command line put 2 arguments 
    if len(sys.argv) == 3:
        deck_one = sys.argv[1]
        deck_two = sys.argv[2]
        
        
        
    # Assigns trainer 1 name, health, and deck
    trainer1 = Trainer("Trainer 1", 100)
    
    # Assigns trainer 2 name, health, and deck
    trainer2 = Trainer("Trainer 2", 100)
    
    # error is not this solution (loading in the decks)
    for i in load_animon(deck_one):
        trainer1.add_card_to_deck(i)
    for i in load_animon(deck_two):
        trainer2.add_card_to_deck(i)
    
    
    #shuffle's deck
    trainer1.shuffle_deck()
    trainer2.shuffle_deck()
    

    # prints out the beginnig stack data 
    print(trainer1)
    print(trainer2)
    print()

    # creates arena as arenatime and starts game
    arenatime = Arena(trainer1, trainer2)
    arenatime.play_game()
    
    # Prints the Battle log 
    for battle in arenatime.get_battle_log():
        print(battle)
    print()
    
    print(arenatime.save_log("battlelog.txt"))
    
    
  
