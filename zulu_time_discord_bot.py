#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 14:36:45 2020

@author: jonnyteronni
"""


import discord
from discord.ext import commands
import pytz #Timezones library
from datetime import datetime
import pandas as pd

client = commands.Bot(command_prefix = '!')

# info = commands.Context(author)

def getKey(val):
   for key, value in pytz.country_timezones.items():
      if val == value:
         return key
      return "Country doesn't exist"

def convert_time_to_utc():
    print('')




@client.event
async def on_ready():
    print('Bot is running.')

@client.command()
async def zulu(ctx):
    await ctx.send('{} just wrote something'.format(ctx.message.author.name))
    
@client.command()
async def regtimezone(ctx):
    # tz = pytz.country_timezones(country)
    await ctx.send(ctx)
    
    
@client.event
async def on_message(message):
    if message.author == client.user:
        return
   	# standard list of timezones for given time.
   	# timezone_var = pickle.load( open( "tzdata.p", "rb" ) )


    # register user timezone
    if message.content.startswith('!regtimezone'):
        msg = str(message.content)
        msg = msg.split()
        msg = " ".join(msg[1:])
        user_tz = msg
        if user_tz not in pytz.common_timezones:
            await message.channel.send('Error: {} is not a timezone.'.format(user_tz))
        else:
            await message.channel.send(user_tz)



    # # register user timezone
    # if message.content.startswith('!regtimezone'):
    #     msg = str(message.content)
    #     msg = msg.split()
    #     msg = " ".join(msg[1:])
    #     user_country_code = getKey(msg)
    #     print(user_country_code)
    #     if user_country_code not in pytz.country_timezones.keys():
    #         await message.channel.send('Error: {} is not a timezone.'.format(msg))
    #     else:
    #         user_tz = pytz.timezone(user_country_code)
    #         await message.channel.send(user_tz)
    
    
    # # register user timezone
    # if message.content.startswith('!regtz'):
    #     msg = str(message.content)
    #     msg = msg.split()
    #     msg = " ".join(msg[1:])
    #     user_tz = 'Etc/{}'.format(msg)
    #     if user_tz not in pytz.all_timezones:
    #         await message.channel.send('Error: {} is not a timezone.'.format(msg))
    #     else:
    #         # tz = pytz.country_timezones[msg]
    #         # print(tz)
    #         await message.channel.send(user_tz)
        
    # if message.content.startswith('!timezones'):
    #     await message.channel.send(pytz.country_timezones.keys())
      
        
        
        
        
        
        
    # report local and zulu time to user
    if message.content.startswith('!zulutime'):
        utc = pytz.utc
        
        # filter message without command
        msg = str(message.content)
        msg = msg.split()
        msg = " ".join(msg[1:])
        
        # add ETC for timezone code
        user_tz = 'Etc/{}'.format(msg)
        
        
        # create report with zulu (UTC) and user local timezone
        final_msg = ("Zulu: ",str(datetime.now(utc)),'\n', "Local: ", str(datetime.now(pytz.timezone(user_tz))))
        report = ''.join(final_msg)
                
        await message.channel.send(report)



    # print all timezones available to user
    if message.content.startswith('!timezones'):
       
        final_msg = "Please check your TZ database name on https://en.wikipedia.org/wiki/List_of_tz_database_time_zones (third column)\ne.g. 'Europe/London'"
        await message.channel.send(final_msg)
        
        
# #We delete default help command
# client.remove_command(‘help’) #Embeded help with list and details of commands
# @client.command(pass_context=True)
# async def help(ctx):
#     embed = discord.Embed(
#         colour = discord.Colour.green())
#     embed.set_author(name='Help : list of commands available')
#     embed.add_field(name='.ping', value='Returns bot respond time in milliseconds', inline=False)
#     embed.add_field(name='.quote', value='Get inspired by a powerful quote', inline=False)
#     await ctx.send(embed=embed)


  
client.run('NzYzNzU5ODgzOTI5Mzg3MDE4.X38Y0g.Qz5taVCAVgglyLcbhnZ-xHq3EQg')


# timezone-bot

# import discord
# from discord.ext import commands

# from datetime import datetime
# from pytz import timezone

# description = '''A bot to be used for converting a time in UTC to zones used by other members of the discord.
# Usage requires the format like this - 2009-05-05 22:28 '''
# bot = commands.Bot(command_prefix='!', description=description)

# @bot.event
# async def on_ready():
#     print('Logged in as')
#     print(bot.user.name)
#     print(bot.user.id)
#     print('------')

# @bot.command()
# async def timeNow(): #formerly printCurrentTime
#     fmt = "%Y-%m-%d %H:%M:%S %Z%z"

#     # Current time in UTC
#     now_utc = datetime.now(timezone('UTC'))
#     await bot.say (now_utc.strftime(fmt) + " (UTC)")

#     # Convert to Europe/London time zone
#     now_london = now_utc.astimezone(timezone('Europe/London'))
#     await bot.say (now_london.strftime(fmt) + " (London)")

#     # Convert to Europe/Berlin time zone
#     now_berlin = now_utc.astimezone(timezone('Europe/Berlin'))
#     await bot.say (now_berlin.strftime(fmt) + " (Berlin)")

#     # Convert to CET time zone
#     now_cet = now_utc.astimezone(timezone('CET'))
#     await bot.say (now_cet.strftime(fmt) + " (CET)")

#     # Convert to Israel time zone
#     now_israel = now_utc.astimezone(timezone('Israel'))
#     await bot.say (now_israel.strftime(fmt) + " (Israel)")

#     # Convert to Canada/Eastern time zone
#     now_canada_east = now_utc.astimezone(timezone('Canada/Eastern'))
#     await bot.say (now_canada_east.strftime(fmt) + " (Canada/Eastern)")

#     # Convert to US/Central time zone
#     now_central = now_utc.astimezone(timezone('US/Central'))
#     await bot.say (now_central.strftime(fmt) + " (US/Central)")

#     # Convert to US/Pacific time zone
#     now_pacific = now_utc.astimezone(timezone('US/Pacific'))
#     await bot.say (now_pacific.strftime(fmt) + " (US/Pacific)")


# @bot.command()
# async def convertTime(date_str): #formerly printFutureTime #this will only work with a UTC time, so work this out in advance
#     #date_str = "2009-05-05+22:28"
#     datetime_obj = datetime.strptime(date_str, "%Y-%m-%d+%H:%M")

#     fmt = "%Y-%m-%d %H:%M %Z%z"

#     # Current time in UTC
#     now_utc = datetime_obj.replace(tzinfo=timezone('UTC'))
#     await bot.say (now_utc.strftime(fmt) + " (UTC)")

#     # Convert to Europe/London time zone
#     now_london = now_utc.astimezone(timezone('Europe/London'))
#     await bot.say (now_london.strftime(fmt) + " (London)")

#     # Convert to Europe/Berlin time zone
#     now_berlin = now_utc.astimezone(timezone('Europe/Berlin'))
#     await bot.say (now_berlin.strftime(fmt) + " (Berlin)")

#     # Convert to CET time zone
#     now_cet = now_utc.astimezone(timezone('CET'))
#     await bot.say (now_cet.strftime(fmt) + " (CET)")

#     # Convert to Israel time zone
#     now_israel = now_utc.astimezone(timezone('Israel'))
#     await bot.say (now_israel.strftime(fmt) + " (Israel)")

#     # Convert to Canada/Eastern time zone
#     now_canada_east = now_utc.astimezone(timezone('Canada/Eastern'))
#     await bot.say (now_canada_east.strftime(fmt) + " (Canada/Eastern)")

#     # Convert to US/Central time zone
#     now_central = now_utc.astimezone(timezone('US/Central'))
#     await bot.say (now_central.strftime(fmt) + " (US/Central)")

#     # Convert to US/Pacific time zone
#     now_pacific = now_utc.astimezone(timezone('US/Pacific'))
#     await bot.say (now_pacific.strftime(fmt) + " (US/Pacific)")

# bot.run('NzYzNzU5ODgzOTI5Mzg3MDE4.X38Y0g.akoZ-llF7wFHVTqHx7KLG3r69v8')



##from pytz import all_timezones ##this prints out all available time zones
##
##print (len(all_timezones))
##for zone in all_timezones:
##    print (zone)


# Europe/London
# CET
# Israel
# Canada/Eastern 
# US/Central 