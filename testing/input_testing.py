"""testing inputs so you dont throw shit in the programm"""

def test_string(string, expection):
    """tests user inputs, maybe not needed in final version
    arg:
        string: the input that needs to be tested
        expection: the input it should be"""
    
    if expection == 'name':
        lenght = len(string)
        if lenght == 0:
            print("You made no input.")
            return False
        if lenght <= 15:
            return True
        if lenght > 15:
            print("Your input is to long. Max letters are 15")
            return False
        
    if string in expection:
            return True
    else:
        print("Your input wasnt correct.")
        return False
        
def test_int(string, expection):
    
    if expection == "None":
        try:
            val = int(string)
            return True
        except ValueError:
            print("You have to insert a number.")
            return False
    
    try:
        val = int(string)
        if val in expection:
            return True
        if val in expection:
            print("Your input wasnt valid.")
            return False
    except ValueError:
        print("You have to insert a number.")
        return False
            