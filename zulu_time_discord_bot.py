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



# define bot and prefix
client = commands.Bot(command_prefix = '!')


# Check on terminal if bot is running
@client.event
async def on_ready():
    print('Bot is running.')

    
# For every message on channel bot will check if the message starts with specific commands
@client.event
async def on_message(message):
        

    # if bot is the author of the message
    if message.author == client.user:
        return


    # discord command for register user timezone on database
    if message.content.startswith('!regtimezone'):
        
        # exclude command from the message
        msg = str(message.content)
        msg = msg.split()
        msg = " ".join(msg[1:])
        
        # define user timezone
        user_tz = msg
        
        # check if timezone exists
        if user_tz not in pytz.common_timezones:
            await message.channel.send('Error: {} is not a timezone.'.format(user_tz))
        
        
        # if user timezone exists
        else:
            
           
            # gets info from DB into a dataframe
            timezones_df = SQL_cnx.connect_to_timezones_table()
            
            
            # checks if username already exists on DB
            if message.author.name in timezones_df['username'].values:
                
                # changes timezone on DB for username
                SQL_cnx.update_user_timezone(message.author.name,user_tz)
                
                await message.channel.send('Timezone defined as {} for {}.'.format(user_tz, message.author.name))
            
            
            # insert new user on DB if he does not exist yet
            else:
                
                SQL_cnx.insert_user_timezone(message.author.name,user_tz)    
            
                await message.channel.send('Timezone defined as {} for {}.'.format(user_tz, message.author.name))
                
                
                
                
                
                
    # discord command for user to check current timezone on DB            
    if message.content.startswith('!checktimezone'):
        
        # gets info from DB into a dataframe
        timezones_df = SQL_cnx.connect_to_timezones_table()
        
        # checks if username already exists on DB
        if message.author.name in timezones_df['username'].values:
            
            # creates dictionary with username and timezone
            timezones_dict = dict(zip(timezones_df['username'],timezones_df['timezone']))
            
            # define user timezone
            user_tz = timezones_dict[message.author.name]
            
            await message.channel.send("{}'s timezone is registered as {}.".format(message.author.name,user_tz))
        
        # if user does not exist on db
        else: 
            
             await message.channel.send("{} has no timezone registered. Please use !regtimezone 'timezone' ".format(message.author.name))
    
    
    
    
        
    # discord command to report local and zulu time to user
    if message.content.startswith('!zulutime'):
        
        # get utc timezone
        utc = pytz.utc
        
        # exclude command from the message
        msg = str(message.content)
        msg = msg.split()
        msg = " ".join(msg[1:])
        
        # gets info from DB into a dataframe
        timezones_df = SQL_cnx.connect_to_timezones_table()
        
        # create report with zulu (UTC) and user local timezone
               
        # define zulutime and format to hh:mm
        zulutime = "{:d}:{:02d}".format(datetime.now(utc).hour,datetime.now(utc).minute) 
        
        # create discord object
        embed = discord.Embed(
                colour = discord.Colour.green())
        
        # checks if username already exists on DB
        if message.author.name in timezones_df['username'].values:
            
            # define user timezone
            user_tz = timezones_df[timezones_df['username']==message.author.name]['timezone'].values[0]    
            
            # define local time using user timezone and format to hh:mm
            localtime = "{:d}:{:02d}".format(datetime.now(pytz.timezone(user_tz)).hour,datetime.now(pytz.timezone(user_tz)).minute)
            
            # add lines to discord object
            embed.add_field(name='Zulu', value=zulutime, inline=False)
            embed.add_field(name='Local', value=localtime, inline=False)
                 
            
        # if user does not exist on db report only zulutime
        else:
            
            # add lines to discord object
            embed.add_field(name='Zulu', value=zulutime, inline=False)
                      
               
        await message.channel.send(embed=embed)




    # discord command to print all timezones available to user
    if message.content.startswith('!timezones'):
       
        final_msg = "Please check your TZ database name on https://en.wikipedia.org/wiki/List_of_tz_database_time_zones (third column)\ne.g. 'Europe/London'"
        
        await message.channel.send(final_msg)
        







        
    # Delete default help command
    client.remove_command('help') #Embeded help with list and details of commands
    
    # discord command to show a help object describing all bot commands
    if message.content.startswith('!help'):
        
        # create discord object
        embed = discord.Embed(
            colour = discord.Colour.green())
        
        # add lines to discord object
        embed.set_author(name='Help : list of commands available')
        embed.add_field(name='!regtimezone', value="Register your timezone on bot:\n1) Check your timezone with !timezones command\n2) use !regtimezone 'your time zone'", inline=False)
        embed.add_field(name='!timezones', value='Get list of all timezones to choose from.', inline=False)
        embed.add_field(name='!checktimezone', value='Check your timezone registered on bot.', inline=False)
        embed.add_field(name='!zulutime', value='Check zulu and your local time.', inline=False)
        
        await message.channel.send(embed=embed)
  
        


  
client.run('Token here')