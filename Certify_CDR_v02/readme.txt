Install and Set up information.

Simply copy paste the Certify_CDR folder where
you have admin rights. You will need to manually
kick off the DB create process. See below for
the simple direction to get that started.
You can get flask working immediately by following
the quick instruction or host on a webserver.

Do not run FLASK using the debug option in
production.
---------------------------------------------
Run Flask
---------------------------------------------
using
$env:FLASK_APP = "certifycdr.py"
$env:FLASK_DEBUG=1

flask run --host=0.0.0.0 for outside to reach
To properly host this application you will
need to consult FLASK documentation. I will
be attempting to host on both an APACHE and
an IIS server I will update the readme at
a later date with those directions.
---------------------------------------------
To create DB
---------------------------------------------
run the create.py file

---------------------------------------------
To migrate DB
---------------------------------------------
run the migrate.py file

---------------------------------------------
To upgrade DB
---------------------------------------------
run the upgrade.py file

---------------------------------------------
To downgrade DB
---------------------------------------------
run the downgrade.py file

--------------------------------------------
The import of CAR files from CUCM
--------------------------------------------
You will need to have your CAR files dumped
to the inserts directory. The script will
find the location of these files and import
them into the database once created
