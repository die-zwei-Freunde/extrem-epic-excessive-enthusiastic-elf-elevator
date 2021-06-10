"""testing inputs so you dont throw shit in the programm"""
from logger import printf

def test_string(string, expection):
    """tests user inputs, maybe not needed in final version
    arg:
        string: the input that needs to be tested
        expection: the input it should be"""
    
    if expection == 'name':
        lenght = len(string)
        if lenght == 0:
            printf("You made no input.")
            return False
        if lenght <= 15:
            return True
        if lenght > 15:
            printf("Your input is to long. Max letters are 15")
            return False
        
    if string in expection:
            return True
    else:
        printf("Your input wasnt correct.")
        return False
        
def test_int(string, expection):
    if string in expection:
        return True
    else:
        printf("Your input wasnt valid.")
        return False
