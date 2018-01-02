Author: A. Nihiser | apnihiser@gmail.com | https://github.com/merkkie/

DISCLAIMER: This is still very rough and insecure, do not run in any production environments!!!

VISION: To create a script that will allow reporting against a Cisco Call Manager version 10.5.2.12901-1 (tested against).

Current Functionality: Updated the original script into a full blown application that includes the following modules.
  1) SQLite3 Database
  2) Flask Framework
  3) Flask-SQLalchemy interaction between web GUI and database
  4) Basic Forms to collect report paramenters.
  5) Flask-Security
  6) Python general scripting to hold it all together.
  
Current Status: Full steam ahead. Have just completed the logic that allows the web GUI to both send and receive data from the database.
Very limited reporting only based on Unix Time Stamps. I will combine the old CUCMCDR logic that converted CAR process data into human-readable reporting. 

Any comments or questions about this project please reach out to me and I'll see what I can do to implement or answer any questions.

Installation: 

1)


Credits: I based much of the flask programming from both https://pythonprogramming.net/ and https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
