# python createdbandtable.py
import sqlite3

conn = sqlite3.connect('stdb.db')
print ("Opened stdb.db successfully");
print ("stdb.db資料庫開設成功");

conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print ("Table created successfully");
conn.close()