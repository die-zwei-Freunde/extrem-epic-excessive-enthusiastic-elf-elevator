"""testing inputs so you dont throw shit in the programm"""
from logger import printf
import classes.race as cr
import classes.alignment as ca


def test_quantaty(inp):

    condition = True
    while condition:
        try:
            inp = int(inp)
            if inp in range(1, 10):
                 condition = False
            else:
                inp = input("You need to pick a number between 1 and 9, please try again: ")
        except:
            inp = input("Your input wasn't an integer, please try again: ")
    return inp


def test_races(inp):

    condition = True
    while condition:
        if inp in cr.__all__:
            condition = False
        else:
            inp = input(f"Your input wasn't correct, please try again. {cr.__all__}: ")
    return inp.capitalize()


def test_alignment(inp):

    condition = True
    while condition:
        if inp in ca.__all__:
            condition = False
        else:
            inp = input(f"Your input wasn't correct, please try again. {ca.__all__}: ")
    return inp.capitalize()