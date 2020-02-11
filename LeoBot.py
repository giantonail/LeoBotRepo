# -*- coding: utf-8 -*-
"""
Created on Thu Jan 23 17:33:18 2020

@author: jupiter
"""

import os
import random
import mytype
import scorekeep
import asyncio
from PIL import Image
from vsimage import multi_imageconcat
import configparser

import discord
from dotenv import load_dotenv
global fighting


load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    activ = discord.Game('Nintendogs™')
    await client.change_presence(activity=activ)
    



@client.event
async def on_message(message):
    global fighting
    if message.author == client.user:
        return

    if 'slut' in message.content.lower():
        await message.channel.send('Did somebody say slut?')
        
    if message.content == '!myaesthetic':
        await message.channel.send('{} your aesthetic is {} {} {}.'.format(message.author.mention,*mytype.whataesthet()))
    
    if message.content == '!mytype':
        urtype = mytype.whattype()
        if len(urtype) == 3:
            await message.channel.send('{} you are {} {} {} type!'.format(message.author.mention,*urtype))
        else:
            await message.channel.send('{} you are {} {} type!'.format(message.author.mention,*urtype))
    if message.content == '!myclass':
        await message.channel.send('{}, you are a level {} {} {} with {}.'.format(message.author.mention,
                                   random.randint(1,20),*mytype.whatclass()))
    


    if message.content == '!myscore':
        config = configparser.ConfigParser()
        config.read('betgame.ini')
        if config['FIGHT']['fighting'] == 'True':
            await message.channel.send('Fight underway, wait until it\'s over.')
            return
        score = scorekeep.readscore(str(message.author))
        await message.channel.send('Your score is {}'.format(score))

        
        
        
        
        
        
    if message.content == '!fight':
        scorekeep.fightgame()
        config = configparser.ConfigParser()
        config.read('betgame.ini')
        p1f = config['FIGHT']['p1f']
        p2f = config['FIGHT']['p2f']
        p1n = config['FIGHT']['p1n']
        p2n = config['FIGHT']['p2n']
        await message.channel.send('The {} is fighting the {}! ({}:{})'.format(p1f,p2f,p1n,p2n))
        im1 = Image.open('fight_image\{}.jpg'.format(p1f))
        vs = Image.open('fight_image\divider.jpg')
        im2 = Image.open('fight_image\{}.jpg'.format(p2f))
        im_list = [im1,vs,im2]
        multi_imageconcat(im_list).save('fightimage.jpg')
        await message.channel.send(file=discord.File('fightimage.jpg'))
        await asyncio.sleep(60)
        config.read('betgame.ini')
        winner = config['FIGHT']['winner']
        await message.channel.send('The {} won!'.format(winner))
        config.set('FIGHT', 'winner', '')
        config.set('FIGHT', 'loser', '')
        config.set('FIGHT', 'p1f', '')
        config.set('FIGHT', 'p2f', '')
        config.set('FIGHT', 'p1n', '')
        config.set('FIGHT', 'p2n', '')
        config.set('FIGHT','betters','')
        config.set('FIGHT', 'fighting', 'False')
        with open('betgame.ini', 'w+') as configfile:
            config.write(configfile)
        
    if message.content.startswith('!bet'):
        config = configparser.ConfigParser()
        config.read('betgame.ini')
        betters = config['FIGHT']['betters']
        if str(message.author) in betters:
            await message.add_reaction('👎')
            await asyncio.wait(0.5)
            await message.channel.send('You already bet.')
            return
        if not config.has_option('USERS',str(message.author)):
            await message.channel.send('Adding {}...'.format(message.author.mention))
            scorekeep.readscore(str(message.author))
        winner = config['FIGHT']['winner']
        loser = config['FIGHT']['loser']
        if winner == '':
            await message.channel.send('Fights done, go home.')
            return
        messlst = message.content.lower().split()
        if len(messlst) != 3:
            await message.add_reaction('👎')
            return
        if not messlst[2].isdigit():
            await message.add_reaction('👎')
            return
        fighter = messlst[1]
        bet = int(messlst[2])
        currentscore = int(scorekeep.readscore(str(message.author)))
        if currentscore <= 0:
            currentscore = 1000
        if bet > currentscore:
            await message.add_reaction('👎')
            return
        if bet <= 0:
            await message.add_reaction('👎')
            return
        if fighter != winner and fighter != loser:
            await message.add_reaction('👎')
            return
        await message.add_reaction('👍')
        config.set('FIGHT','betters','{} {}'.format(config['FIGHT']['betters'], str(message.author)))
        with open('betgame.ini','w+') as configfile:
            config.write(configfile)
        if fighter == winner:
            p1f = config['FIGHT']['p1f']
            p2f = config['FIGHT']['p2f']
            p1n = int(config['FIGHT']['p1n'])
            p2n = int(config['FIGHT']['p2n'])
            if winner == p1f:
                scorekeep.writescore(str(message.author), currentscore + bet * (p2n/p1n))
            else:
                scorekeep.writescore(str(message.author), currentscore + bet * (p1n/p2n))            
        else:
            scorekeep.writescore(str(message.author), currentscore - bet)

        
    if message.content == '!lb':
        config = configparser.ConfigParser()
        config.read('betgame.ini')
        if config['FIGHT']['fighting'] == 'True':
            await message.channel.send('Fight underway, wait until it\'s over.')
            return
        board = scorekeep.leaderboard()
        lbmess = ''
        for i in range(len(board)):
            tempstr = '{}. {} {}\n'.format(len(board)-i,board[i][0],board[i][1])
            lbmess += tempstr
        await message.channel.send(lbmess)
    
    if message.content == '!leohelp':
        helpmess = '!myaesthetic - assigns your aesthetic\n!mytype - assigns your Pokemon type\n!myscore - displays your current LeoBets score\n!fight - begins a LeoBets fight\n!bet {fighter} {amount} - places bet on LeoBets fight\n!leaderboard - displays current LeoBets leaderboard'
        await message.channel.send(helpmess)
        
        
        
        

client.run(token)




















