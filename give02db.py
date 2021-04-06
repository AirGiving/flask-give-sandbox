# -*- coding: UTF-8 -*-
#python give02db.py


import sqlite3
conn=sqlite3.connect("give02db.db")#建立資料庫
cursor = conn.cursor()
sql = '''Create table users(  
        number INTEGER,
        name String,
        email String,
        phone String,
        date DateTime,
        primary key("number" autoincrement)
        )'''
cursor.execute(sql)                     # 執行SQL指令
cursor.close()      
conn.close()