import os
import datetime
import sqlite3
import csv

"""
CUCMCDR.py

Author: A.Nihiser, apnihiser@gmail.com, Github: https://github.com/merkkie/CUCMCDR

Purpose: This entire script has been copy pasted into the new and improved CUCMCAR
script. In a nutshell the script creates the required CDR & CMR databases automatically
by pulling from 2 text documents. 2 other txt docs allow the data transfer to occure
between DB and the CMR & CDR records. These docs and the path to them may need to be 
modified to fit in your environment depending on where your CMR, CDR documents are 
being downloaded to, and version of Call Manager. I am running 10.5.2.12901-1.

There is a pruning process that drops records after 60 days.

All UNIX datestamps have been converted to a new easily readable format, and IPs
are automatically converted as well.

lastly all data is pulled and deleted from the chosen directory, in this case I am 
using C:\CDR_Working_DIR. Once again this path may need to be changed
depending on where your records are located.

As of now we can view all CDR & CMR data by using SQLite3 databrowswer. Much more planned

Future: Creating a Flask front end to interact and display data currently researching the
best path to bring this alive in a smart and effective manner. I'd like to provided data
searching, analytics and quality reports that can be searched by individual calls, daily,
weekly, monthly time increments.

"""

def main():

    conn = sqlite3.connect('car.db')
    c = conn.cursor()

    create_table_cmr(c)
    create_table_cdr(c)

    path = 'C:\CDR_Working_DIR'
    dirs = os.listdir( path )

    for files in dirs:

        path = "C:\CDR_Working_DIR\{}".format(files)

        with open(path, 'rt', newline='') as f:

            reader = csv.reader(f, delimiter=',')

            rows = list(reader)

            f.close()

            os.remove(path)

            for row in rows:

                if row[0][0] == "0" or row[0][0] == "1":
                    row[4] = datetime.datetime.utcfromtimestamp(  # Timestamp Convert
                        int(row[4])).strftime('%Y-%m-%d %H:%M:%S')

                    list_of_dec = [  # Submit the csv columns which
                                    int(row[7]),  # contain IPs needing converted
                                    int(row[13]),
                                    int(row[21]),
                                    int(row[28]),
                                    int(row[35]),
                                    int(row[43])
                                  ]

                    x_list = [convert_ips(dec) for dec in list_of_dec]

                    [
                        row[7],   # create x_list and assign those values to
                        row[13],  # the working CSV file
                        row[21],
                        row[28],
                        row[35],
                        row[43]
                    ] = x_list
                    data_entry_cdr(c, row)

                elif row[0][0] == "2":

                    row[6] = datetime.datetime.utcfromtimestamp(  # Timestamp Convert
                        int(row[6])).strftime('%Y-%m-%d %H:%M:%S')

                    data_entry_cmr(c, row)
    db_purge(c)

    conn.commit()

    c.close()

    conn.close()


def db_purge(c):

    c.execute("""DELETE FROM cdrtable WHERE dateTimeOrigination < DATETIME('now','-60 day')""")
    c.execute("""DELETE FROM cmrtable WHERE dateTimeStamp < DATETIME('now','-60 day')""")


def convert_ips(signed32BitInt):

    if signed32BitInt == 0:
        return "0"

    hexValue = hex(signed32BitInt & (2**32-1))[2:10]

    if len(hexValue) == 7:
        hexValue = '0' + hexValue

    elif len(hexValue) == 6:
        hexValue = '00' + hexValue

    elif len(hexValue) == 5:
        hexValue = '000' + hexValue

    hexSwap = [hexValue[6:8], hexValue[4:6], hexValue[2:4], hexValue[0:2]]

    return '.'.join([str(int(n,16)) for n in hexSwap])


def create_table_cmr(c):

    cmrt = open('cmr_t.txt', 'r')
    cmrTable = cmrt.read()
    c.execute("""CREATE TABLE IF NOT EXISTS cmrtable ({})""".format(cmrTable))


def data_entry_cmr(c, cmr_data_row):

    cdrd = open('cmr_d.txt', 'r')
    cmrData = cdrd.read()
    c.execute("""INSERT INTO cmrtable ({}) VALUES (
                                                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                                                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                                                    ?,?,?,?,?,?,?,?,?,?,?,?
                                                   )""".format(cmrData), (cmr_data_row))


def create_table_cdr(c):

    cdrt = open('cdr_t.txt', 'r')
    cdrTable = cdrt.read()
    c.execute("""CREATE TABLE IF NOT EXISTS cdrtable ({})""".format(cdrTable))


def data_entry_cdr(c, cdr_data_row):

    cdrd = open('cdr_d.txt', 'r')
    cdrData = cdrd.read()
    c.execute("""INSERT INTO cdrtable ({}) VALUES (
                                                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                                                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                                                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                                                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                                                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                                                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                                                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                                                    ?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,
                                                    ?
                                                   )""".format(cdrData), (cdr_data_row))


if __name__ == '__main__':
    main()
