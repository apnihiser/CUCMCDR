import csv
import datetime
import os, sys
from os.path import exists


"""
CUCMCDR.py
Author: A.Nihiser, apnihiser@gmail.com, Github: https://github.com/merkkie/CUCMCDR

Purpose: After numerous jobs, no billing servers and manually looking up cdr
requestsfor 4+ years I've decided to put together a python script for my very
first python project.

Current Functionality: Manually download CDRs for now. Run the script from
powershell. Example below. Script will convert POSIX Timestamps into a Human
Readable format. All IP addresses will be converted as well. Search for any
dialed number to pull each row that matches.

Future: I would like to build a proper billing server, with a web front end to
allow granular searches. Instead of parsing CSVs a mySQL db. This is all as I
learn so the more experienced python users will find this code raw and
unsophisticated but I am open to any critism to make this project legitamite
for all to use.

Thanks to Jay Swan at http://unroutable.blogspot.com for the example that helped
me crack the signed 32-bit integer problem with hex().

To utilize this script perform the following:
1.) Run in a powershell script
2.) Submit 3 arguments
    a.) The location and name of the input file. Either txt or csv.
    b.) The location and name of the output file. txt or csv.
    c.) The called number you are searching for.

See the following example:
python CUCMCDR.py 'C:\CDR.txt' 'C:\911output.csv' 911

"""


def conversion(working_csv):

    for row in working_csv:
        if row[30] == sys.argv[3]:      #Search for user provided called number.

            row[4] = datetime.datetime.utcfromtimestamp(      #Timestamp Convert
                int(row[4])).strftime('%Y-%m-%d %H:%M:%S')

            list_of_dec = [                     #Submit the csv columns which
                           int(row[7]),         #contain IPs needing converted
                           int(row[13]),
                           int(row[21]),
                           int(row[28]),
                           int(row[35]),
                           int(row[43])
                           ]

            x_list = [convert_ips(dec) for dec in list_of_dec]

            [
            row[7],             #create x_list and assign those values to
            row[13],            #the working CSV file
            row[21],
            row[28],
            row[35],
            row[43]
            ] = x_list

            final_copy(row)


def convert_ips(signed32BitInt):

    if signed32BitInt == 0:
        return "CDR returned 0 as IP"

    hexValue = hex(signed32BitInt & (2**32-1))[2:10]

    if len(hexValue) == 7:
        hexValue = '0' + hexValue

    hexSwap = [hexValue[6:8], hexValue[4:6], hexValue[2:4], hexValue[0:2]]

    return '.'.join([str(int(n,16)) for n in hexSwap])


def final_copy(final_csv):

    if not exists(sys.argv[2]):
        with open(sys.argv[2], 'a', newline='') as csvFinal:
            writer = csv.writer(csvFinal)
            writer.writerow(csvHeader)
            writer.writerow(final_csv)
    else:
        with open(sys.argv[2], 'a', newline='') as csvFinal:
            writer = csv.writer(csvFinal)
            writer.writerow(final_csv)


if __name__ == '__main__':

    with open(sys.argv[1], 'rt', newline='') as csvfile:    #open raw csv.
        reader = csv.reader(csvfile, delimiter=',')
        csvHeader = next(reader)
        unfilterdcsv = list(reader)

        conversion(unfilterdcsv)
