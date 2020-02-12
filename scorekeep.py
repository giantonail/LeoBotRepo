# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 13:31:15 2020

@author: jupiter
"""

import configparser
import random

def writescore(author, score):
    config = configparser.ConfigParser()
    config.read('betgame.ini')
    cutscore = round(score)
    config.set('USERS', str(author), str(cutscore))
    with open('betgame.ini', 'w+') as configfile:
        config.write(configfile)
        

def readscore(author):
    authstr = str(author)
    config = configparser.ConfigParser()
    config.read('betgame.ini')
    if config.has_option('USERS',authstr):
        return config['USERS'][author]
    else:
        config.set('USERS', authstr, '1000')
        with open('betgame.ini', 'w+') as configfile:
            config.write(configfile)
        return readscore(author)
    
def leaderboard():
    config = configparser.ConfigParser()
    config.read('betgame.ini')
    userstup = config.items('USERS')
    users = [list(elem) for elem in userstup]
    for i in range(len(users)):
        users[i][0] = users[i][0].translate({ord(ch): None for ch in '#0123456789'})
        users[i][1] = int(users[i][1])
    users.sort(key = lambda x: x[1])
    return users


def fightgame():
    config = configparser.ConfigParser()
    config.read('betgame.ini')
    fighters = config.items('FIGHTERS')
    p1 = random.choice(fighters)
    p2 = random.choice(fighters)
    while p1 == p2:
        p2 = random.choice(fighters)
    p1f = p1[0]
    p2f = p2[0]
    p1n = p1[1]
    p2n = p2[1]
    config.set('FIGHT', 'p1f', p1f)
    config.set('FIGHT', 'p2f', p2f)
    config.set('FIGHT', 'p1n', p1n)
    config.set('FIGHT', 'p2n', p2n)
    config.set('FIGHT', 'fighting', 'True')
    ftn = random.randint(1,int(p1n)+int(p2n))
    if ftn <= int(p1n):
        config.set('FIGHT', 'winner', p1f)
        config.set('FIGHT', 'loser', p2f)
    else:
        config.set('FIGHT', 'winner', p2f)
        config.set('FIGHT', 'loser', p1f)
    with open('betgame.ini', 'w+') as configfile:
        config.write(configfile)
        