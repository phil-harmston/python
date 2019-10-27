import dbconnection
import sqlite3

with open("fixedpricelist.txt", 'r') as f:
    line = f.readlines()

if dbconnection.createTable():
    try:
        for i, l in enumerate(line):
            data = l.split(',')
            dbconnection.writer(*data)
            if (i % 100 == 0):
                dbconnection.con_commit()
        dbconnection.con_commit()
    except sqlite3.IntegrityError as e:
        print("Sqlite Integrity Error " + str(e))

