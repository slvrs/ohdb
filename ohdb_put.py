import sys
import importlib
import sqlite3

if len(sys.argv) < 3:
    sys.stderr.write("OHDB Put: Not enough arguments")
    sys.exit()

config = importlib.import_module("ohdb_config")
conn = sqlite3.connect(config.db_file)

cursor = conn.cursor()
cursor.execute(""" 
        create table if not exists data
        (name text primary key, val text)
        """)

cursor.execute("replace into data(name, val) values (?, ?)",
        (sys.argv[1], sys.argv[2]))
conn.commit()

