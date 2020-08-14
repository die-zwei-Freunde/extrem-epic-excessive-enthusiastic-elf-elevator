from classes.playerc import playerclass as pc
import start_setup as setup
from classes.enemy import goblin as gb

#import game_loop as gl


players = setup.setup_player()
#setup.setup_world()


#players, _ = setup.start_setup()
#piwo = pc.Player('Piwo', 'orc', 'fighter')
#jan = pc.Player('Jan', 'human', 'mage')
#players = [piwo, jan]

print(players)

#gl.Game_loop()

goblinsky = gb.BasicGoblin('Gertrud')
print(goblinsky)

#print(players[0].stat_display())
#print(players[1].stat_display())

#print('Enemy 1: ', '\n', goblinsky.stat_display())
