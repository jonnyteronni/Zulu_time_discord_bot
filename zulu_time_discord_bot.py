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
import SQL_connection as SQL_cnx

client = commands.Bot(command_prefix = '!')



def getKey(val):
   for key, value in pytz.country_timezones.items():
      if val == value:
         return key
      return "Country doesn't exist"




@client.event
async def on_ready():
    print('Bot is running.')


  
    
    
@client.event
async def on_message(message):
    
    
    
    # if bot is the author of the message
    if message.author == client.user:
        return





    # register user timezone
    if message.content.startswith('!regtimezone'):
        msg = str(message.content)
        msg = msg.split()
        msg = " ".join(msg[1:])
        user_tz = msg
        
        # Check if timezone exists
        if user_tz not in pytz.common_timezones:
            await message.channel.send('Error: {} is not a timezone.'.format(user_tz))
        
        else:
            
            # Gets info from DB into a dataframe
            timezones_df = SQL_cnx.connect_to_timezones_table()
            
            # timezones_dict = dict(zip(timezones_df['username'],timezones_df['timezone']))
            
            # Checks if username already exists on DB
            if message.author.name in timezones_df['username'].values:
                
                # Changes timezone on DB for username
                
                SQL_cnx.update_user_timezone(message.author.name,user_tz)
                
                # timezones_df.loc[(timezones_df['username']==message.author.name)] = user_tz
                
                await message.channel.send('Timezone defined as {} for {}.'.format(user_tz, message.author.name))
            
            else:
                
                SQL_cnx.insert_user_timezone(message.author.name,user_tz)    
            
                await message.channel.send('Timezone defined as {} for {}.'.format(user_tz, message.author.name))
                
                
                
                
                
                
    # For user to check current timezone on DB            
    if message.content.startswith('!checktimezone'):
        
        timezones_df = SQL_cnx.connect_to_timezones_table()
        
        if message.author.name in timezones_df['username'].values:
            timezones_df = SQL_cnx.connect_to_timezones_table()
            
            timezones_dict = dict(zip(timezones_df['username'],timezones_df['timezone']))
            
            user_tz = timezones_dict[message.author.name]
            
            await message.channel.send("{}'s timezone is registered as {}.".format(message.author.name,user_tz))
        
        else: 
            
             await message.channel.send("{} has no timezone registered. Please use !regtimezone 'timezone' ".format(message.author.name))
    
    
    
    
        
    # report local and zulu time to user
    if message.content.startswith('!zulutime'):
        utc = pytz.utc
        
        # filter message without command
        msg = str(message.content)
        msg = msg.split()
        msg = " ".join(msg[1:])
        
        # Gets info from DB into a dataframe
        timezones_df = SQL_cnx.connect_to_timezones_table()
        
        # create report with zulu (UTC) and user local timezone
               
        
        zulutime = "{:d}:{:02d}".format(datetime.now(utc).hour,datetime.now(utc).minute) 
        
        
        embed = discord.Embed(
                colour = discord.Colour.green())
        
        if message.author.name in timezones_df['username'].values:
            
            
            user_tz = timezones_df[timezones_df['username']==message.author.name]['timezone'].values[0]    
                        
            localtime = "{:d}:{:02d}".format(datetime.now(pytz.timezone(user_tz)).hour,datetime.now(pytz.timezone(user_tz)).minute)
            
            # embed.set_author(name='Help : list of commands available')
            embed.add_field(name='Zulu', value=zulutime, inline=False)
            embed.add_field(name='Local', value=localtime, inline=False)
                       
        
        else:
            
            embed.add_field(name='Zulu', value=zulutime, inline=False)
                       
               
        await message.channel.send(embed=embed)










    # print all timezones available to user
    if message.content.startswith('!timezones'):
       
        final_msg = "Please check your TZ database name on https://en.wikipedia.org/wiki/List_of_tz_database_time_zones (third column)\ne.g. 'Europe/London'"
        await message.channel.send(final_msg)
        







        
    # Delete default help command
    client.remove_command('help') #Embeded help with list and details of commands
    
    if message.content.startswith('!help'):

        embed = discord.Embed(
            colour = discord.Colour.green())
        embed.set_author(name='Help : list of commands available')
        embed.add_field(name='!regtimezone', value='Register your timezone on bot.', inline=False)
        embed.add_field(name='!timezones', value='Get list of all timezones to choose from.', inline=False)
        embed.add_field(name='!checktimezone', value='Check your timezone registered on bot.', inline=False)
        embed.add_field(name='!zulutime', value='Check zulu and your local time.', inline=False)
        await message.channel.send(embed=embed)
        # await message.channel.send("Help command")    
        
        
        
        



  
client.run('Token goes here')