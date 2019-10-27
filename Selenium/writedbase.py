import sqlite3
import time

"""function to connect to the database"""
# Use os. to check for dbase folder if not present create it before creating database.
con = sqlite3.connect('./dbase/uabc.db')
c = con.cursor()
def writedb(**args):
    CS_CODE, CON_SIZE, CASE_PACK, PRODUCT_NAME, STATUS, COST_OZ, CURRENT_RETAIL, NEW_RETAIL, COMMENT, CAT, DESCRIPTION = args
    # print(CS_CODE)

def testdata(*args):

    largs = list(args)
    for i, a in enumerate(largs):
        if i == 0:
            if a.isnumeric() and (len(a) == 6):
                pass
            else:
                print("SKU is invalid")
                #print(a)
        if i == 1:
            if a.isnumeric() and (len(a) <= 5):
                pass
            else:
                print("Size is invalid")
                print(largs[0])
        if i == 2:
            if a.isnumeric() and (len(a) <= 2):
                size = a
                #print(a)
        if i == 3:
            if (a.find("ml") == -1):
                #print(args)
                newval = a + " " + args[1] + "ml"
                largs[largs.index(a)] = newval

    largs = largs[0:4]

    return largs







    # is the second arg a number four or less in length

    # is the thrid arg a number on or two in length

    # is the 4th a complete product discription including the bottle size.

def main():
    fwrite = open("fixedpricelist.txt", "a+")
    ferror = open("baddata.txt", "a+")
    cur = con.cursor()

    fread = open("pricelist.txt")
    data = []
    f = fread.readlines()
    for line in f:
        line = line.strip("\n")

        d = line.split(",")

        # this if statement fixes the ml column problem



        flist = testdata(*d)
        if (len(flist)==0):
            pass
        else:            #time.sleep(1)
            my_data = ",".join([str(x) for x in flist])
            fwrite.write(my_data + "\n")


   # print("my_data")


    fwrite.close()
    fread.close()


if __name__== "__main__":
    main()
