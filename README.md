CUCMCDR.py
Author: Adam Nihiser, apnihiser@gmail.com, Github: https://github.com/merkkie/CUCMCDR

Purpose: After numerous jobs, no billing servers and manually looking up cdr requests
for 4+ years I've decided to put together a python script for my very first python
project.

Current Functionality: Manually download CDRs for now. Run the script from powershell.
Example below. Script will convert POSIX Timestamps into a Human Readable format. All
IP addresses will be converted as well. Search for any dialed number to pull each 
row that matches.

Future: I would like to build a proper billing server, with a web front end to allow
granular searches. Instead of parsing CSVs a mySQL db. This is all as I learn so
the more experienced python users will find this code raw and unsophisticated but I am
open to any critism to make this project legitamite for all to use.

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
