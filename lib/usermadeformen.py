import json

usermade = {}


def add_item(name, nodes):
    usermade[name] = nodes


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
