Author: A. Nihiser | apnihiser@gmail.com | https://github.com/merkkie/

DISCLAIMER: This is still very rough and insecure, do not run in any production environments!!!

VISION: To create a script that will allow reporting against a Cisco Call Manager version 10.5.2.12901-1 (tested against).

Current Functionality: Updated the original script into a full blown application that includes the following modules.
  1) SQLite3 Database
  2) Flask Framework
  3) Flask-SQLalchemy interaction between web GUI and database
  4) Basic Forms to collect report paramenters.
  5) Python general scripting to hold it all together.
  
Current Status: Full steam ahead. Have just completed the logic that allows the web GUI to both send and receive data from the database.
Very limited reporting only based on Unix Time Stamps. I will combine the old CUCMCDR logic that converted CAR process data into human-readable reporting. 

Any comments or questions about this project please reach out to me and I'll see what I can do to implement or answer any questions.

Installation: 

  1) I am assuming that if you are at this point you understand at least the basics of Python and how to install, work with pip and         import modules and install a VENV environment into your projects. If I can help please let me know, just understand I have only been working in python myself for about 4 months now so I will not have answers to all questions!
  2) I have tried to strip any branding from this project so if you would like you can upload your 200x200 images to the base.html template and update HTML data to reflect your organization.
  3) import the required modules: $ flask\Scripts\pip install flask
                                  $ flask\Scripts\pip install flask-sqlalchemy
                                  $ flask\Scripts\pip install sqlalchemy-migrate
                                  $ flask\Scripts\pip install flask-wtf
                                  # if I am forgetting anything please let me know
  4) As far as how you are serving your website is up to you. I have been running this in a dev environment using flask. If you would like to do the same you can go ahead and run "run.py" to browse to the page http://localhost:5000/.
  5) This will bring you to the homepage. From this point you will notice that there is no database to search and no real functionality to the website. Let's fix that.
  6) To create the database run db_create.py. I would recommend reading the database section from miguiel grinberg's blog entry below it goes step by step on the logic. If you ever need to upgrade & migrate to a new structure all the necessary information is presented below.
  7) I am currently working to integrate my existing DBinterface.py script into this project currently you will need to test off that DB.
  8) I am assuming you have a directory that your CUCM CAR process is dumping files into.
  9) Edit DBinterface.py to point to whichever directory those files reside in.
 10) Run DBinterface.py and it will process and delete those files (save copies if you want to create seperate DBs to test). DBinterface.py will delete any records older than 60days from the DB.
 11) Once the database is in place and the website is up and running make sure to place the db into the main certify_cdr directory, you should now be able to query those records by time stamp from http://localhost:5000/cdr.
 12) Yes there are probably bugs and it doesn't look pretty one of the many issues to hash out. I work on this daily so if there is anyone out there that wants more progress on this project please let me know and I'll upload to GITHUB.COM at a faster pace.
 
 In The Future: LDAP integration with Active Directory, HTTPS, Secure Logins, Form Validation, Pretty GUI, Ironed out Logic, AJAX, and more that I'm not remember or too lazy to list out!!!

Credits: I based much of the flask programming from both https://pythonprogramming.net/ and https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
