from classes.action.battle import BattleAction
from classes.action.loot import TreasureAction
from classes.action.null import NullAction

CLASSES = {'battle': BattleAction,
           'null': NullAction,
           'loot': TreasureAction}