import classes.action as ca

class ActionManager:
    def __init__(self, actionary):
        self.type = actionary['type']

        self.action = ca.CLASSES[self.type](**actionary)

    def start(self, players):
        return self.action.start(players)



def main():
    from classes.playerc import playerclass
    p = playerclass.Player('ME', 'Human', 'Mage')
    ps = {p.name: p}
    loot = ['Runic Staff of Horror']
    enemy = ['Basic Goblin', 'Basic Goblin', 'Tank Goblin']

    am = ActionManager({'type': 'battle', 'loot': loot, 'enemy': enemy})
    am.start(ps)

if __name__ == '__main__':
    main()