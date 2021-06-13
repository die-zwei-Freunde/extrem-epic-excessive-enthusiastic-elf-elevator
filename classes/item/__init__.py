from classes.item.equip.mage import RunicStaff, CrookedWand, RodOfHellfire, WandOfAvalon
from classes.item.equip.fighter import BloodyGlovesOfDemiGodJan, StandardDagger, Stillet, BloodCloakDagger
from classes.item.equip.jewlery import RingOfMagic, RingOfPower, EarringOfDefense

from classes.item.use.potion import SmallHealthPotion

__all__ = ['RunicStaff', 'BloodyGlovesOfDemiGodJan', 'SmallHealthPotion']
CLASSES = {'Runic Staff of Horror': RunicStaff,
           'Wand': CrookedWand,
           'Bloody Gloves of a Demi-God': BloodyGlovesOfDemiGodJan,
           'Rod of Hellfire': RodOfHellfire,
           'Wand of Avalon': WandOfAvalon,
           'Stillet': Stillet,
           'Blood Cloak Dagger': BloodCloakDagger,
           'Dagger': StandardDagger,
           'Ring of Magic': RingOfMagic,
           'Ring of Power': RingOfPower,
           'Earring of Defense': EarringOfDefense,
           'Small health potion': SmallHealthPotion}