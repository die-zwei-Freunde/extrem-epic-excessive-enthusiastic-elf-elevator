import numpy as np
from logger import printf
import time

from classes.dice import die


class BattleManager():
    '''
    This class handles all the battling.
    Gets a new set of enemies and players for each battle.
    '''
    def __init__(self, players, enemies):
        self.players = players
        self.enemies = enemies
        self.die = die.D20()

        self.all_players = {}
        for players in self.players:
            self.all_players[players.name] = players

    def run(self):
        counter = 1

        printf('Battle starts!')
        while self.players and self.enemies:
            printf('- Round {}'.format(counter))
            self.battle(counter)
            counter += 1
            for players in self.players:
                self.all_players[players.name] = players

        if self.players:
            printf('Congrats! You won!')

            return self.all_players, True
        elif self.enemies:
            printf('You lost, man.')
            return self.all_players, False


    def battle(self, counter):
        actors = []
        for player in self.players:
            if counter % player.INIT == 0:# and player.INIT <= counter:
                actors.append((player, self.players.index(player)))
        for enemy in self.enemies:
            if counter % enemy.INIT == 0: #and enemy.INIT <= counter
                actors.append((enemy, self.enemies.index(enemy)))

        for act in actors:
            actor, actor_index = act
            if actor not in self.enemies and actor not in self.players:
                continue
            printf('It is {}s turn to attack! [HP: ({}/{})]'.format(actor.name, actor.HP, actor.MAX_HP))
            target, t_id, t_index = self.choose_target(actor)
            skill = self.choose_skill(actor)
            if type(skill) == int:
                return 0
            dmg, buff, debuff = self.act(actor, skill, target)

            self.apply(actor, actor_index, target, t_index, dmg, buff, debuff)
            time.sleep(2)

            self.check_for_dead()

        self.reduce_cooldown()

    def apply(self, actor, act_id, target, target_id, dmg, buff, debuff):
        if buff:
            printf('Not yet implemented!')
        if debuff:
            printf('Not yet implemented!')

        #TODO implement dice feature

        if target in self.players:
            self.players[target_id].decrease_stat('HP', dmg)
            current_HP = self.players[target_id].HP

        if target in self.enemies:
            self.enemies[target_id].decrease_stat('HP', dmg)
            current_HP = self.enemies[target_id].HP

        if current_HP < 0:
            current_HP = 0

        printf('\n {} deals {} points of damage to {}. [HP: ({}/{})]\n'.format(actor.name,
                                                                               dmg,
                                                                               target.name, current_HP, target.MAX_HP))

    def _apply_die(self, luck):
        eye = self.die.roll(luck)

        # die policy:
        if eye == 0:
            printf(' That was a weak attack!')
            return 0.75
        elif eye == 20:
            printf(' That was a critical attack!')
            return 1.25
        elif 15 >= eye >= 19:
            return 1.15
        elif 2 >= eye >= 5:
            return 0.85
        else:
            return 1

    def act(self, actor, skill, target):
        dmg, des, buff, debuff = skill.get_damage()
        attval = getattr(actor, des)
        if des == 'ATT':
            res = 'DEF'
        if des == 'MAG':
            res = 'RES'
        defval = getattr(target, res)

        # HERE IS WHERE THE FANCY MATH STUFF WOULD HAPPEN

        eff_att = attval + dmg
        eff_att *= self._apply_die(actor.LUCK)
        if defval < eff_att:
            val = np.abs(defval - eff_att)
        else:
            val = 0

        return int(val), buff, debuff


    def check_for_dead(self):
        for player in self.players:
            if player.HP <= 0:
                printf('Oh no! Player {} died!\n'.format(player.name))
                self.players.remove(player)
                player.HP = 1
                self.all_players[player.name] = player

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
                    dmg, des, _, _ = skill.get_damage()
                    eff_dmg = dmg + getattr(player, des)
                    string += str(skill) + f'\n Effective damage (before damage calc): {eff_dmg}\n'
            
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
                s = f'-- Enemy: {act.name} - HP: {act.HP} - Debuff: None - Buff: None\n'
                string += s

            name = input(string)
            try:
                for target in target_list:
                    if target.name == name:
                        break
                flag = False
            except:
                printf('That did not work, wrong name. Try again.')

        return target, target.name, target_list.index(target)

    def reduce_cooldown(self):
        for player in self.players:
            player.apply_cooldown('')
            
