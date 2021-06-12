from classes.item.equip.mage import RunicStaff, CrookedWand
from classes.item.equip.fighter import BloodyGlovesOfDemiGodJan, StandardDagger

from classes.item.use.potion import SmallHealthPotion

__all__ = ['RunicStaff', 'BloodyGlovesOfDemiGodJan', 'SmallHealthPotion']
CLASSES = {'Runic Staff of Horror': RunicStaff,
           'Wand': CrookedWand,
           'Bloody Gloves of a Demi-God': BloodyGlovesOfDemiGodJan,
           'Dagger': StandardDagger,
           'Small health potion': SmallHealthPotion}