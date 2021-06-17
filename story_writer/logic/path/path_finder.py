import json


def path_finder(world):
    tree_G = []
    tree_color = []

    with open('classes/world/story/' + world + '/config.json', 'r') as fp:
        config = json.load(fp)
        fp = config['fp']

    keys = [key for key in config.keys()][1:]
    len_keys = max([len(key) for key in keys])

    root = int(config[''].strip('world'))

    for i in range(0, len_keys + 1):
        ind_keys = [key for key in keys if len(key) == i]

        for key in ind_keys:

            tup1 = int(config[key].strip('world'))

            with open(fp + config[key] + '.json', 'r') as f:
                dic = json.load(f)

            action = dic['action']['type']

            if dic['Endpoint']:
                tree_color.append('red')
            else:
                if action == 'battle':
                    tree_color.append('blue')
                if action == 'loot':
                    tree_color.append('green')
                if action == 'null':
                    tree_color.append('yellow')

            decision = dic['decision']

            if decision != {}:
                dec_keys = [dec for dec in decision.keys()]
                for dec in dec_keys:
                    flag = key + dec
                    tup2 = int(config[flag].strip('world'))
                    tree_G.append((tup1, tup2))

    return tree_G, tree_color, root





