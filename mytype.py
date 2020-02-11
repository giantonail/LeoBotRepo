# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 19:22:18 2020

@author: jupiter
"""
import random

def whattype():
    typelist = ['normal 😐','fighting 👊','flying 🌬️','poison ☠️','ground ⛰️','rock 🗿','bug 🐛','ghost 👻'\
                ,'steel 🔩','fire 🔥','water 💦','grass 🌱','electric ⚡','psychic 👁‍','ice ❄️','dragon 🐉','dark 🌙','fairy ✨']
    type1 = random.choice(typelist).capitalize()
    ran = random.randint(1,100)
    if ran < 25:
        type2 = random.choice(typelist).capitalize()
        while type1 == type2:
            type2 = random.choice(typelist).capitalize()
        if type1 == 'Electric ⚡' or type1 == 'Ice ❄️':
            return ['an', type1, type2]
        else:
            return ['a', type1, type2]
    elif type1 == 'Electric ⚡' or type1 == 'Ice ❄️':
        return ['a', type1]
    else:
        return ['a', type1]
    
def whataesthet():
    adjf = open('adjectives.txt','r')
    adjectives = adjf.readlines()
    adjf.close()
    nounf = open('nouns.txt','r')
    nouns = nounf.readlines()
    nounf.close()
    
    adj1 = random.choice(adjectives)
    adj2 = random.choice(adjectives)
    while adj1 == adj2:
        adj2 = random.choice(adjectives)
    noun = random.choice(nouns)
    
    return adj1.rstrip('\n'),adj2.rstrip('\n'),noun.rstrip('\n')

def whatclass():
    racef   = open('races.txt','r')
    races   = racef.readlines()
    racef.close()
    
    classf  = open('classes.txt','r')
    classes = classf.readlines()
    classf.close()
    
    quirkf  = open('quirks.txt','r')
    quirks  = quirkf.readlines()
    quirkf.close()
    
    race    = random.choice(races).rstrip('\n')
    clas    = random.choice(classes).rstrip('\n')
    quirk   = random.choice(quirks).rstrip('\n')
    return race, clas, quirk

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
