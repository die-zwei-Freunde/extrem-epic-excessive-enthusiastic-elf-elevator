import numpy as np
from logger import printf

class BattleManager():
    '''
    This class handles all the battling.
    Gets a new set of enemies and players for each battle.
    '''
    def __init__(self, players, enemies):
        self.players = players
        self.enemies = enemies

    def run(self):
        counter = 1

        printf('Battle starts!')
        while self.players and self.enemies:
            printf('- Round {}'.format(counter))
            self.battle(counter)
            counter += 1

        if self.players:
            printf('Congrats! You won!')
            return True
        elif self.enemies:
            printf('You lost, man.')
            return False


    def battle(self, counter):
        actors = []
        for player in self.players:
            if player.INIT % counter == 0 and player.INIT <= counter:
                actors.append((player, self.players.index(player)))
        for enemy in self.enemies:
            if enemy.INIT % counter == 0 and enemy.INIT <= counter:
                printf(enemy.INIT >= counter)
                actors.append((enemy, self.enemies.index(enemy)))

        for act in actors:
            actor, actor_index = act
            printf('It is {}s turn to attack!'.format(actor.name))
            target, t_id, t_index = self.choose_target(actor)
            skill = self.choose_skill(actor)
            dmg, buff, debuff = self.act(actor, skill, target)

            self.apply(actor, actor_index, target, t_index, dmg, buff, debuff)

        self.check_for_dead()
        


    def apply(self, actor, act_id, target, target_id, dmg, buff, debuff):
        if buff:
            printf('Not yet implemented!')
        if debuff:
            printf('Not yet implemented!')

        printf('\n {} deals {} points of damage to {}.\n'.format(actor.name,
                                                                dmg,
                                                                target.name))

        if target in self.players:
            current_HP = self.players[target_id].HP
            self.players[target_id].change_stat('HP', current_HP - dmg)

        if target in self.enemies:
            current_HP = self.enemies[target_id].HP
            self.enemies[target_id].change_stat('HP', current_HP - dmg)
   
 
    def act(self, actor, skill, target):
        dmg, des, buff, debuff = skill.get_damage()
        attval = getattr(actor, des)
        if des == 'ATT':
            res = 'DEF'
        if des == 'MAG':
            res = 'RES'
        defval = getattr(target, res)

        # HERE IS WHERE THE FANCY MATH STUFF WOULD HAPPEN

        if defval < attval:
            val = dmg
        else:
            val = 0

        return val, buff, debuff


    def check_for_dead(self):
        del_array = []
        for player in self.players:
            if player.HP <= 0:
                printf('Oh no! Player {} died!\n'.format(player.name))
                self.players.remove(player)
        for enemy in self.enemies:
            if enemy.HP <= 0:
                printf('Ha! Enemy {} died!\n'.format(enemy.name))
                self.enemies.remove(enemy)
            


    def choose_target(self, actor):
        if actor in self.players:
            target_list = self.enemies
            act_id = 'player'
        elif actor in self.enemies:
            target_list = self.players
            act_id = 'enemy'
        else:
            raise ValueError('Problem when choosing target.')

        if act_id == 'player':
            target, target_id, target_index = self._player_choice(target_list)
        elif act_id == 'enemy':
            target = target_list[np.random.randint(len(target_list))]
            target_id = target.name
            target_index = target_list.index(target)

        return target, target_id, target_index

        


    def choose_skill(self, player):
        if player in self.players:
            act_id = 'player'
        if player in self.enemies:
            act_id = 'enemy'
        
        skills = player.get_skills()
        skill_dict = {}
        for skill in skills:
            if skill.is_available():
                skill_dict[skill.name] = skill
        if not skill_dict:
            printf('All your skills are on cooldown. You cannot move, fam.\n')
            return 0

        if act_id == 'player':

            flag = True
            while flag:
                string = ''' Select (by name) the skill you want to apply
    from the list below:\n \n'''
                for skill in skill_dict.values():
                    string += str(skill)
            
                name = input(string)
                try:
                    skill = skill_dict[name]
                    flag = False
                except:
                    printf('That did not work, wrong name. Try again.')

            player.apply_cooldown(name)

        elif act_id == 'enemy':
            skill = list(skill_dict.values())[np.random.randint(len(skill_dict.values()))]

        return skill

    def _player_choice(self, target_list):
        flag = True
        while flag:
            
            string = ''' Select (by name) your target from the list below:\n'''
            for act in target_list:
                string += str(act)

            name = input(string)
            try:
                for target in target_list:
                    if target.name == name:
                        break
                flag = False
            except:
                printf('That did not work, wrong name. Try again.')

        return target, target.name, target_list.index(target)
            
