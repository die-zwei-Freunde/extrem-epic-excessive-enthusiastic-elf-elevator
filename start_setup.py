"""Handels the game setup"""

import os
from classes.playerc import playerclass as pc
from testing import input_testing as inp
from logger import printf
import classes.race as cr
import classes.alignment as ca


def start_setup():
    """Plays intro and calls the player set up
    returns a list with the player objects"""

    intro()

    players = setup_player()

    quest = quest_line()

    return players, quest


def intro():
    printf("""You're about to enter the world of Jan and Piwo.
These are the gods of this world. Whatever you do, do not anger them!""")


def setup_player():
    """sets up the players in the playerclass
    returns a list with player objects"""

    player_quantity = input("How many players are you? ")
    player_quantity = inp.test_quantaty(player_quantity)

    players = {}
    for i in range(1, player_quantity + 1):
        name = input(f"Player {i} whats your name? ")
        name = name.capitalize()

        race_list = cr.__all__
        race = input(f"""Hello {name}, what race do you want to be?
{race_list} """)
        race = race.capitalize()
        race = inp.test_races(race)

        alignment_list = ca.__all__
        alignment = input(f"""And what will be your alignment?
{ca.__all__} """)
        alignment = alignment.capitalize()
        alignment = inp.test_alignment(alignment)

        p = pc.Player(name, race, alignment)
        players[name] = p
        
    return players


def quest_line():

    subfolders = [f.name for f in os.scandir('classes/world/story') if f.is_dir()]
    counter = []
    for i, folder in enumerate(subfolders):
        printf(f"[{i}] : ", folder)
        counter.append(f'{i}')

    quest = input('What questline do you wanna choose? ')
    quest = inp.test_quest(quest, counter)

    return subfolders[quest]