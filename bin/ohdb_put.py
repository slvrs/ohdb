import sys
import importlib

if len(sys.argv) < 3:
    sys.stderr.write("OHDB Put: Not enough arguments")
    sys.exit()

db = importlib.import_module("ohdb_db")
conn = db.connect()
cursor = conn.cursor()
cursor.execute("replace into data(name, val) values (?, ?)",
        (sys.argv[1], sys.argv[2]))
conn.commit()

