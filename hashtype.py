#!/bin/python3
import core

def hashtype(hash_):
    for i in range(len(hash_)):
        if hash_[i] not in core.element["HEX"]:
            print(core.element["DISPLY"]["ERROR"])
            return 1

    if len(hash_)==32:
        print(core.element["DISPLY"]["HASH"][0])
        return core.element["TYPE"][0]
    elif len(hash_)==40:
        print(core.element["DISPLY"]["HASH"][1])
        return core.element["TYPE"][1]
    elif len(hash_)==56:
        print(core.element["DISPLY"]["HASH"][2])
        return core.element["TYPE"][2]
    elif len(hash_)==64:
        print(core.element["DISPLY"]["HASH"][3])
        return core.element["TYPE"][3]
    elif len(hash_)==96:
        print(core.element["DISPLY"]["HASH"][4])
        return core.element["TYPE"][4]
    elif len(hash_)==128:
        print(core.element["DISPLY"]["HASH"][5])
        return core.element["TYPE"][5]
    else:
        print(core.element["DISPLY"]["ERROR"])
        return 1
