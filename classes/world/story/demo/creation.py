import json

name = 'world11'

prestring = 'Prepare to die.'

action_type = 'battle'
enemy = ['GodPiwo']
loot = []
poststirng = ''

decision = {}
decision['a'] = 'Prepare to die.'

config = {}
config['prestring'] = prestring
config['action'] = {}
config['action']['type'] = action_type
config['action']['enemy'] = enemy
config['action']['loot'] = loot

config['poststring'] = poststirng
config['decision'] = decision

config['Endpoint'] = True

with open(f'./{name}.json', 'w') as fp:
    json.dump(config, fp, indent=4)