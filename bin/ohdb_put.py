import sys
import importlib

if len(sys.argv) < 3:
    sys.exit("OHDB Put: Not enough arguments")

db = importlib.import_module("ohdb_db")
conn = db.connect()
cursor = conn.cursor()
cursor.execute("replace into data(name, val) values (?, ?)",
        (sys.argv[1], sys.argv[2]))
conn.commit()

