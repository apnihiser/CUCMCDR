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

1) Decide how your going to host your application. I'm going to try to provide instructions for hosting on both apache and IIS, so I'll get back to you on that. For the meantime if you need to get this up and going there are many instructions available for getting flask hosted in all sorts of places.

1) Create a Virtual Environment if needed

2) Install Modules, I installed the following:
    a) Flask
    b) flask-SQLalchemy
    c) Flask-Migrate
    d) flask-Security
2) Create your Database.
    a) run create.py to create the DB
    b) migrate.py and update.py to make any changed to your database created from create.py
    c) downgrade will do exactly what it says revert your last migration
    d) for more information on this please see https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iv-database
3) Config your config.py file.
    a) You can change the name of the DB
    b) Set your SECRET_KEY for CSRF security
    c) Change your login Hash and Salt Parameters.
4) Set your environmental variables for powershell $env:FLASK_APP = "certifycdr.py"
5) Create your DB
    a) After step 4 is complete run flask db init from the \CertifyCDR directory


Credits: I based much of the flask programming from both https://pythonprogramming.net/ and https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
