Author: A.Nihiser, apnihiser@gmail.com, Github: https://github.com/merkkie/CUCMCDR
Purpose: This entire script has been copy pasted into the new and improved CUCMCAR
script. In a nutshell the script creates the required CDR & CMR databases automatically
by pulling from a few text documents. These docs and the path to them may need to be 
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
