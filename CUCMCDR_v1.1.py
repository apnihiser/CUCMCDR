import csv
import datetime
import os, sys
from os.path import exists
from stat import *

"""
CUCMCDR.py
Author: Adam Nihiser, apnihiser@gmail.com, Github: https://github.com/merkkie/CUCMCDR
Purpose: After downloading CDR from CUCM, CUCMCDR.py, once executed
will search the CDR document and return each example in a row. The datetime
origin will also be converted from Epoch time. The use case this filled for me
was creating monthly reports of each 911 call to submit to management.
Thanks to Jay Swan at http://unroutable.blogspot.com for the example that helped
me crack the signed 32-bit integer problem with hex().

To utilize this script perform the following:
1.) Run in a powershell script
2.) Submit 2 arguments
    a.) The location and name of the input file. Either txt or csv
    b.) The location and name of the output file. txt or csv

See the following example:
python CUCMCDR.py 'C:\CDR.txt' 'C:\911output.csv'
"""

def main():
    csvFilesRe()

def csvFilesRe():

    with open(sys.argv[1], 'rt', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        csvHeader = next(spamreader)
        csvlist = list(spamreader)
        CPNdnis(csvlist, csvHeader)


def CPNdnis(csvlist, csvHeader):

    for dn in csvlist:
        if dn[30] == sys.argv[3]:
            timeConvert(dn, csvHeader)


def timeConvert(theFile, csvHeader):

    theFile[4] = datetime.datetime.utcfromtimestamp(
            int(theFile[4])).strftime('%Y-%m-%d %H:%M:%S')

    ip_origin_dec(theFile, csvHeader)


def ip_origin_dec(theFile, csvHeader):

    list_of_dec = [
                    int(theFile[7]),
                    int(theFile[13]),
                    int(theFile[21]),
                    int(theFile[28]),
                    int(theFile[35]),
                    int(theFile[43])
                    ]

    converted_list = [convert_cdr_hex_ip(dec) for dec in list_of_dec]

    [
    theFile[7],
    theFile[13],
    theFile[21],
    theFile[28],
    theFile[35],
    theFile[43]
    ] = converted_list

    csvFileWr(theFile, csvHeader)


def convert_cdr_hex_ip(signed32BitInt):

    if signed32BitInt == 0:
        return "CDR returned 0 as IP"

    hexValue = hex(signed32BitInt & (2**32-1))[2:10]

    if len(hexValue) == 7:
        hexValue = '0' + hexValue

    hexSwap = [hexValue[6:8], hexValue[4:6], hexValue[2:4], hexValue[0:2]]

    return '.'.join([str(int(n,16)) for n in hexSwap])


def csvFileWr(output, csvHeader):

    if not exists(sys.argv[2]):
        with open(sys.argv[2], 'a', newline='') as csvFinal:
            spamwriter = csv.writer(csvFinal)
            spamwriter.writerow(csvHeader)
            spamwriter.writerow(output)
    else:
        with open(sys.argv[2], 'a', newline='') as csvFinal:
            spamwriter = csv.writer(csvFinal)
            spamwriter.writerow(output)

if __name__ == '__main__':
    main()
