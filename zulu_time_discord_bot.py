#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:36:45 2020

@author: jonnyteronni
"""


import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.')


@client.event

async def asdsadas:
    print('Bot is working')
    
client.run('')