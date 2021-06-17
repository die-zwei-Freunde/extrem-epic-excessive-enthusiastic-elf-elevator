import json

name = 'world13'

prestring = 'You face the Light-God of this world, Jan. Prepare to die.'

action_type = 'battle'
enemy = ['GodJan']
loot = []
poststirng = 'Do not anger the gods of creation.'

decision = {}

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