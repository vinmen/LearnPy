#! /usr/bin/env python

import sys

def readFile(filepath):
    with open(filepath) as f:
        lines = f.read().splitlines()
    for line in lines:
        print(line)

def getArgs(args):
    for arg in args:
        print(arg)

if __name__ == "__main__":
    getArgs(sys.argv)
    readFile("alarm.txt")
