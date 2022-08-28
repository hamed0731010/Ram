import re
from flask import Flask
import sqlite3    
import os
import threading
from datetime import datetime

 #procees for claculate the ram status
def ram():  
# Getting memory config
    threading.Timer(60,ram).start()
    total_memory, used_memory, free_memory = map(
    int, os.popen('free -t -m').readlines()[-1].split()[1:])
    date=datetime.now()
    tu=(total_memory,used_memory,free_memory,date)
    create_ram_config(tu)
    

#Create the table
def tb_create():
    conn = sqlite3.connect('ram.db') 
    conn.execute('''CREATE TABLE Client_db
                ( total int,
                    used int,
                    free int,
                    data text
                );''') 
    
    conn.commit() 
    conn.close()
#fill the table
def create_ram_config(tup):
    conn = sqlite3.connect('ram.db')
    cursor = conn.cursor()
    params = tup
    cursor.execute("INSERT INTO Client_db VALUES (?,?,?,?)",params)
    conn.commit()
    print('cofig Creation Successful')
    conn.close()
#read from table of db   
def read_db(n):
    conn = sqlite3.connect('ram.db')
    cursor = conn.cursor()
    sql='SELECT * FROM Client_db ORDER BY data DESC LIMIT  '+str(n)
    cursor.execute(sql)
    rows=cursor.fetchall()
    conn.close()
    li=[]
    #convert list to dict in the list
    for i,row in enumerate( rows):
        dict={}
        dict.update({i+1:row})
        li.append(dict)    
    return li





