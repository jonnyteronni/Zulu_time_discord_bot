#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 14:07:47 2020

@author: jonnyteronni
"""
import mysql.connector
import pandas as pd

# def create_sql_table(cnx):
#     q_timezones = ("CREATE TABLE IF NOT EXISTS "
#     "7zulu_user_timezones ("
#     "id int NOT NULL AUTO_INCREMENT ,"
#     "username varchar(100) NOT NULL,"
#     "timezone` varchar(100) NOT NULL,"
#     "date` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,"
#     "PRIMARY KEY (`id`));")
    
#     cursor = cnx.cursor()
    
#     cursor.execute(q_timezones)



def connect_to_db():
    #Creating timeseries to export to sql
    # enter your server IP address/domain name
    HOST = "localhost" # "35.192.100.10" # or "domain.com"
    # database name, if you want just to connect to MySQL server, leave it empty
    DATABASE = "7zulu_database"
    # this is the user you create
    USER = "root"
    # user password
    PASSWORD = "2Satisfying!"
    # connect to MySQL server
    
    cnx = mysql.connector.connect(user = USER, password = PASSWORD,host = HOST,
                              database = DATABASE)
    
    try:
        cnx.is_connected()
        print("Connection open")
    
    except print("Connection is not successfully open"):
        pass
    
    # create_sql_table(cnx)
    
    return cnx







def connect_to_timezones_table():
    
    # connect to SQL
    cnx = connect_to_db()
    
    try:
        cursor = cnx.cursor()
        query = ("SELECT * FROM 7zulu_user_timezones;")
        cursor.execute(query)
        results = cursor.fetchall()
    
    except print("Connection to table is not working"):
        pass

    timezones_df=pd.DataFrame(results,columns=["id","username","timezone","date","steamid64","whitelist_id"])
    
    close_sql(cursor,cnx)
    
    return timezones_df


def update_user_timezone(username, timezone):
    # connect to SQL
    cnx = connect_to_db()
    
    try:
        cursor = cnx.cursor()
        query = (f"UPDATE 7zulu_database.7zulu_user_timezones SET timezone = '{timezone}' WHERE username = '{username}';")
        cursor.execute(query)
        cnx.commit()
        
        print("Updated record on table")
        
    except print("Updating table not working"):
        pass
    
    close_sql(cursor,cnx)


def update_user_steamid(username, steamid):
    # connect to SQL
    cnx = connect_to_db()
    
    try:
        cursor = cnx.cursor()
        query = (f"UPDATE 7zulu_database.7zulu_user_timezones SET steamid64 = '{steamid}', whitelist_id = 'Admin={steamid}:whitelist // {username}' WHERE username = '{username}';")
        cursor.execute(query)
        cnx.commit()
        
        print("Updated record on table")
        
    except print("Updating table not working"):
        pass
    
    close_sql(cursor,cnx)



    
def insert_user_timezone(user, tz):
    # connect to SQL
    cnx = connect_to_db()
      
    try:
        cursor = cnx.cursor()
      
        query = ("INSERT INTO 7zulu_database.7zulu_user_timezones (username,timezone) VALUES ({},{});".format("'" + user + "'","'" + tz + "'"))
        
        cursor.execute(query)
        cnx.commit()
        
        print("Inserted new record on table") 
        
    except print("Insert new record on table not working"):
        pass
    
    
    close_sql(cursor,cnx)

def insert_user_steamid(user, steamid):
    # connect to SQL
    cnx = connect_to_db()
      
    try:
        cursor = cnx.cursor()
      
        query = ("INSERT INTO 7zulu_database.7zulu_user_timezones (username,steamid64,whitelist_id) VALUES ({},{},{});".format("'" + user + "'","'" + str(steamid) + "'","'Admin=" + str(steamid) + ":whitelist //" + user + "'"))
        
        cursor.execute(query)
        cnx.commit()
        
        print("Inserted new record on table") 
        
    except print("Insert new record on table not working"):
        pass
    
    
    close_sql(cursor,cnx)


def close_sql(cursor,cnx):
    cursor.close()
    cnx.close()