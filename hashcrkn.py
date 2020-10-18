#!/bin/python3
import core
import hashtype
import online
import itertools
from os import getpid
from os import kill
from sys import argv
from hashlib import *
from signal import SIGKILL
from threading import Thread
from threading import activeCount

def crack(hash_, char, hashtype,min_ = 1, max_ = 13):
    for i in range(min_, max_+1):
        for j in itertools.product(char, repeat=i):
            for k in hashtype:
                if k(''.join(j).encode("utf-8")).hexdigest() == hash_:
                    print(core.element["DISPLY"]["DONE"],"".join(j))
                    Kill()

def wordlist(hash_, wordlist, hashtype):
    with  open(wordlist, 'br') as file_:
        for i in file_.readlines():
            try:
                i = i.replace(b"\n",b"").decode()
                for k in hashtype:
                    if k(i.encode()).hexdigest() == hash_:
                        print(core.element["DISPLY"]["DONE"],i)
                        Kill()
            except:
                pass

def Online(hash_, hashtype):
    for i in online.Check(hash_):
        for k in hashtype:
            if k(i.replace("\n","").encode()).hexdigest() == hash_:
                print(core.element["DISPLY"]["DONE"], i)
                Kill()

def Kill():
    kill(getpid(), SIGKILL)

if __name__ == '__main__':
    try:
        HASHTYPE = hashtype.hashtype(argv[1])
        Thread(target=Online, args=[argv[1], HASHTYPE]).start()
        if HASHTYPE != 1:
            try:
                print(core.element["DISPLY"]["LIST"],argv[2])
                wordlist(argv[1], argv[2], HASHTYPE)
            except:
                print(core.element["DISPLY"]["WITHOUT"])

            for i in ( 'NUM', 'CHARNUM'):
                Thread(target = crack,args =[ argv[1], core.element[i], HASHTYPE]).start()

            print(core.element["DISPLY"]["FUZZ"])
            crack(argv[1], core.element['CHAR'], HASHTYPE)
    except:
        print(core.element["DISPLY"]["HELP"])
        Kill()

