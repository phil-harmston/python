import sqlite3

# Table information
_create_table = "CREATE TABLE LIQUOR ([CS_CODE] TEXT PRIMARY KEY, [CON_SIZE] INTEGER, [CASE_PACK] INTEGER, [PRODUCT_NAME] TEXT)"
con = sqlite3.connect('./dbase/uabc.db')
c = con.cursor()








def close():
    """function to close the database"""
    con.close()


def save():
    """function to save the query string to the database"""
    pass


def read(self):
    """function to read from the database"""
    pass


def createTable():
    """use this to init the database if the database is new"""
    c.execute("""SELECT count(name) FROM sqlite_master WHERE type='table' AND name='LIQUOR'""")
    if (c.fetchone()[0]==1):
        print("Table Exists")
        return True
    else:
        con.execute(_create_table)



def writer(cs, size, case, name):

    #con = sqlite3.connect("./dbase/uabc.db")
    con.execute("INSERT INTO LIQUOR (CS_CODE, CON_SIZE, CASE_PACK, PRODUCT_NAME) VALUES (?, ?, ?, ?)", (cs, size, case, name))



def con_commit():
    con.commit()
    print("insert complete")


def garbage():
    pass

    #connect()
    #cur = con.cursor()
    #cur.execute("SELECT * FROM LIQUOR")
    #rows = cur.fetchall()
    #for row in rows:
    #print(row)
    #con.close()
