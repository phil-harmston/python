import time
import re


def main():
    # open a file to read and one to write
    fread = open("AlphaPriceList.txt", "r")
    fwrite = open("pricelist.txt", "a+")
    # puts the header I want on the file
    #fwrite.write("CS Code, Size, Case Pack, Product Name, Status, Cost/OZ, Current Retail, New Retail, Comment, Category/Description" + "\n")
    # read the file into f
    f = fread.readlines()

    # process the file into something we can use.
    for line in f:
        # don't read anything that doesn't start with a number.
        if line[0].isnumeric():
            # use regex to 2 or more consecutive spaces
            line = re.sub("[ ]{2,}", ",", line)
            # fix and odd ball in the data by replacing the first space with a comma on the case pack
            line = line.replace(" ", ",", 1)
            line = line.strip("\n")
            fwrite.write(line + "\n")
    # close the files
    fread.close()
    fwrite.close()

if __name__ == "__main__":
    main()

