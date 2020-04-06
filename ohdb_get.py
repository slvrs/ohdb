import sys
import importlib
import sqlite3

if len(sys.argv) < 2:
    sys.stderr.write("OHDB Put: Not enough arguments")

config = importlib.import_module("ohdb_config")
conn = sqlite3.connect(config.db_file)

cursor = conn.cursor()
cursor.execute(""" 
        create table if not exists data
        (name text primary key, val text)
        """)

cursor.execute("select val from data where name = ?", (sys.argv[1],))
data = cursor.fetchone()

if data != None:
    print(data[0])
