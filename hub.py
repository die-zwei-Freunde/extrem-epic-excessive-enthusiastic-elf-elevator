from classes.playerc import playerclass as pc
import start_setup as sp
from classes.enemy import goblin as gb
from classes.battle import manager as bl
from logger import printf
import classes.world.worldclass as w
import json


# story = {'prestring': """How could you be so stupid and a bookshelf, when the great god Jan could always watch you.
# He attacks you with all he has. Make yourself ready to die!""",
#          'action': {'type': 'battle', 'loot': [], 'enemy': ['Piwo', 'Jan']},
#          'poststring': """You wont get here!""",
#          'decision': {},
#          'Endpoint': True}
#
# with open('classes/world/story/world07.json', 'w') as fp:
#     json.dump(story, fp, indent=4)

import classes.gameloop.game_loop as gl
g = gl.Game_loop()
g.run()


#players = sp.setup_player()
#goblinsky = gb.BasicGoblin('Gertrud')
#bm = bl.BattleManager(players, [goblinsky])

#piwo = pc.Player('Piwo', 'orc', 'fighter')
#jan = pc.Player('Jan', 'human', 'mage')
#players = [piwo, jan]

#printf(players)

#print([p.skills for p in players])

#gl.Game_loop()
#print(bm.choose_skill(players[0]))
#print([skill.cooldown_counter for skill in players[0].get_skills()])


#printf(bm.run())


#print('Enemy 1: ', '\n', goblinsky.stat_display())