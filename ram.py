from flask import Flask
import psutil
import sqlite3    
import os
import threading
from sqlite3 import Error
from datetime import datetime
# Getting all memory using os.popen()
#x

# Memory usage
#print("RAM memory % used:", round((used_memory/total_memory) * 100, 2))

    
def ram():  
# Getting % usage of virtual_memory ( 3rd field)
    threading.Timer(60,ram).start()
    total= psutil.virtual_memory()[0]
    used=psutil.virtual_memory()[3]
    free=psutil.virtual_memory()[4]
    date_time=datetime.now()
    
    tu_ram=(total,used,free,date_time)
    create_ram_config(tu_ram)

def db_create(db_name):
    conn=None
    try:
        conn=sqlite3.connect(db_name)
        print(conn)
    except Error as e:
            print(e)
    finally:
        if conn :
            conn.close

def db_creat():
    conn = sqlite3.connect('ram.db') #Opens Connection to SQLite database file.
    conn.execute('''CREATE TABLE Client_db
                ( total int,
                    used int,
                    free int,
                    data text
                );''') 
    #Creates the table
    conn.commit() # Commits the entries to the database
    conn.close()

def create_ram_config(tup):
    conn = sqlite3.connect('ram.db')
    cursor = conn.cursor()
    params = tup
    cursor.execute("INSERT INTO Client_db VALUES (?,?,?,?)",params)
    conn.commit()
    print('cofig Creation Successful')
    conn.close()
    
def read_db(n):
    conn = sqlite3.connect('ram.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Client_db ORDER BY data DESC LIMIT  % s ',n )
    rows=cursor.fetchall()
    conn.close()
    li=[]
    for i,row in enumerate( rows):
        dict={}
        dict.update({i+1:row})
        li.append(dict)    
    return li



m=read_db(5)
print(m)
#r=conv_list_json(m)


