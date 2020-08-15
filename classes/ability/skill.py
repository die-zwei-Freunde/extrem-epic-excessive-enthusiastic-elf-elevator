class Skill():
    ''' Abstract base class for skills. '''
    def __init__(self, name='', designation='ATT', attr=None):
        self.name = name
        self.attr = attr

        self.designation = designation

        self.damage = self._setup_damage()
        self.buff, self.debuff = self._setup_effect()
        self.cooldown = self._setup_cooldown()

        self.cooldown_counter = 0
    

    def _setup_damage(self):
        '''
        Return the number of base damage delt
        '''
        raise NotImplementedError()

    def _setup_cooldown(self):
        '''
        Return the number of maximum turns of cooldown.
        '''
        raise NotImplementedError('YOU NEED A COOLDOWN MAAANNN')

    def _setup_effect(self):
        '''
        Edit this method in your skill to give your skill an extra effect'''
        return None, None


    def __repr__(self):
        return 'Skill: {}\n Damage: {}, Attribute: {}, Cooldown: {}\n'.format(\
            self.name, self.damage, self.attr, self.cooldown)


    def is_available(self):
        '''
        Every time this method is used, it is checked
        if the cooldown counter is down to 0.
        If not, reduce the cooldown counter by one.
        Cooldown counter is set up in the setup method.
        '''
        if self.cooldown_counter < 1:
            return True

        else:
            return False

    def reduce_cooldown(self):
        self.cooldown_counter -= 1

    def on_cooldown(self):
        self.cooldown_counter = self.cooldown

    def get_damage(self):
        return self.damage, self.designation, self.buff, self.debuff

    def set_cooldown(self, value):
        self.cooldown = value

    def get_cooldown(self):
        return self.cooldown
