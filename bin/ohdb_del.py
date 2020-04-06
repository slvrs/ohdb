import sys
import importlib

if len(sys.argv) < 2:
    sys.stderr.write("OHDB Put: Not enough arguments")

db = importlib.import_module("ohdb_db")
conn = db.connect()
cursor = conn.cursor()
cursor.execute("delete from data where name = ?", (sys.argv[1],))
conn.commit()

