"""Handels the game setup"""

from classes.playerc import playerclass as pc
from testing import input_testing as inp

def start_setup():
    """Plays intro and calls the player set up
    returns a list with the player objects"""
    
    intro()
    
    players = setup_player()
    
    world = setup_world()
    
    return players, world
    

def intro():
    print("""Myths say this world was created by two almighty beings.
The people of this world call them LMNO and Piwo.
They may guide you on your adventures through the lands of ______.""")



def setup_player():
    """sets up the players in the playerclass
    returns a list with player objects"""
    
    player_quantity = input("How many players are you? ")
    test = inp.test_int(player_quantity, "None")
    while test == False:    
        player_quantity = input("Try again. How many want to play? ")
        test = inp.test_int(player_quantity, "None")
        
    player_quantity = int(player_quantity)
    players = []
    
    for i in range(1, player_quantity + 1):
              
        name = input("Player {} whats your name? ".format(i))
        name = name.capitalize()
        test = inp.test_string(name, 'name')
        while test == False:
            name = input("Pls try again. ")
            name = name.capitalize()
            test = inp.test_string(name, 'name')
            
        
        race = input("""Hello {}, what race do you want to be?
[human, orc] """.format(name))
        race = race.casefold()
        test = inp.test_string(race, ['human', 'orc'])
        while test == False:
            race = input("Pls try again. [human, orc] ")
            race = race.casefold()
            test = inp.test_string(race, ['human', 'orc'])
        
        alignment = input("""And what will be your alignment?
[fighter, mage] """)
        alignment = alignment.casefold()
        test = inp.test_string(alignment, ['fighter', 'mage'])
        while test == False:
            alignment = input("Pls try again. [fighter, mage] ")
            alignment = alignment.casefold()
            test = inp.test_string(alignment, ['fighter', 'mage'])
        
        p = pc.Player(name, race, alignment)
        players.append(p)
        
    return players


def setup_world():
    """selects the questline"""
    
    q1 = "The secret piwo project, jan didn't see :)"
    q2 = "Placeholder"
    questlist = [q1, q2]
    
    print("You have to choose a quest.")
    for i, val in enumerate(questlist):
        print(val, "[{}]".format(i+1))
    
    quest = input("Which of these quests you wanna play? [1,2] ")
    test = inp.test_int(quest, [1, 2])
    while test == False:
        print("The quests are:")
        for i, val in enumerate(questlist):
            print(val, "[{}]".format(i+1))
        quest = input("Which of these quests you wanna play? [1,2] ")
        test = inp.test_int(quest, [1, 2])
    quest = int(quest)
    
    