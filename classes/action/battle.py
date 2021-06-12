from classes.action import action
from classes.battle import manager

import classes.enemy as ce


class BattleAction(action.Action):
    def __init__(self, type, loot, enemy):
        super().__init__(type)

        self.loot = loot
        self.enemy = self._setup_enemies(enemy)

        self.bm = None

    def start(self, players):
        self.bm = manager.BattleManager([p for p in players.values()], self.enemy)

        players, succ = self.bm.run()

        loot = self.loot if succ else []
        return players, loot, succ

    def _setup_enemies(self, enemy):
        done = []
        all = []
        for n, nme in enumerate(enemy):
            name = nme
            if nme in done:
                name += f' {n}'
            en = ce.CLASSES[nme](name=name)
            all.append(en)
            done.append(nme)
        return all


def main():
    from classes.playerc import playerclass
    p = playerclass.Player('ME', 'Human', 'Mage')
    print(p)
    ps = {p.name: p}
    loot = ['Runic Staff of Horror']
    enemy = ['Basic Goblin', 'Basic Goblin', 'Tank Goblin']

    ac = BattleAction('battle', loot, enemy)
    res = ac.start(ps)
    print(res)


if __name__ == '__main__':
    main()

