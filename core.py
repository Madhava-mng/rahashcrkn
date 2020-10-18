#!/bin/python3
from hashlib import *


R = '\u001b[31;1m'
G = '\u001b[32;1m'
Y = '\u001b[33;1m'
N = '\u001b[0m'

element = {
            "DISPLY": {
                "ERROR": f"[{R}TYPE{N}] UnKnown Algorithm",
                "WITHOUT": f"[{Y}CRACKING{N}] With out wordlist",
                "DONE": f"[{G}CRACKED{N}]",
                "NOT": f"[{R}SORRY{N}] Trying with UnKnown hexValue",
                "LIST": f"[{Y}WORDLIST{N}]",
                "HELP": "hashcrkn.py <HASH> <WORDLIST>",
                "FUZZ": f"[{Y}FUZZING{N}] Ascii-Tables",
                "HASH": [
                    f"[{Y}TYPE{N}] md5",
                    f"[{Y}TYPE{N}] sha1",
                    f"[{Y}TYPE{N}] sha224, sha3_224",
                    f"[{Y}TYPE{N}] sha256, sha3_256, blake2s",
                    f"[{Y}TYPE{N}] sha384, sha3_384",
                    f"[{Y}TYPE{N}] sha512, blake2b,sha3_512"]
                    },
            "CHAR": "abcdefghijklmnopqrstuvwxyz ",
            "NUM": "1234567890 ",
            "CHARNUM": "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()-=_+ ",
            "HEX": ['1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f'],
            "TYPE": [
                [md5],[sha1],[sha224,sha3_224],
                [sha256,sha3_256,blake2s],
                [sha384,sha3_384],
                [sha512,blake2b,sha3_512]
                ]
    }
