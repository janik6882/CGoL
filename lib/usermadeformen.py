import json


def writetofile(nodes, name):
    with open('../usermade/usermade.json', 'r') as f:
        config = json.load(f)
    config[name] = nodes
    with open('../usermade/usermade.json', 'w') as f:
        json.dump(config, f)


def loadfromfile(name):
    with open('../usermade/usermade.json', 'r') as f:
        data = json.load(f)
        nodes = data[name]
    return nodes


def umwandeln(nodes):
    minx = nodes[0][1]
    miny = nodes[0][0]
    for i in range(len(nodes)):
        if nodes[i][1] < minx:
            minx = nodes[i][1]
        if nodes[i][0] < miny:
            miny = nodes[i][0]
    for i in range(len(nodes)):
        nodes[i][1] = nodes[i][1] - minx
        nodes[i][0] = nodes[i][0] - miny
    return nodes
