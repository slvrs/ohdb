import sys
import importlib

if len(sys.argv) < 2:
    sys.exit("OHDB Get: Not enough arguments")

db = importlib.import_module("ohdb_db")
conn = db.connect()
cursor = conn.cursor()
cursor.execute("select val from data where name = ?", (sys.argv[1],))
data = cursor.fetchone()

if data != None:
    print(data[0])
