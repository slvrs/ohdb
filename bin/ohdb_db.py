import sqlite3
import os

def connect():
    conn = sqlite3.connect(db_file_name())
    db_init(conn)
    return conn

def db_file_name():
    script_path = os.path.realpath(__file__)
    (script_dir, _) = os.path.split(script_path)
    (common_dir, _) = os.path.split(script_dir)
    return os.path.join(common_dir, "data", "db.db")

def db_init(conn):
    cursor = conn.cursor()
    cursor.execute(""" 
            create table if not exists data
            (name text primary key, val text)
            """)
    cursor.close()
