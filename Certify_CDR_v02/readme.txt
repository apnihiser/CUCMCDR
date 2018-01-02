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

Further information on this:

Let's say that for the next release of your app you have to introduce a change to your models, for example a new table
needs to be added. Without migrations you would need to figure out how to change the schema of your database, both in
your development machine and then again in your server, and this could be a lot of work.

But with database migration support, after you modify the models in your application you generate a new migration
script (flask db migrate), you probably review it to make sure the automatic generation did the right thing, and then
apply the changes to your development database (flask db upgrade). You will add the migration script to source control
and commit it.

--------------------------------------------
The import of CAR files from CUCM
--------------------------------------------
You will need to have your CAR files dumped
to the inserts directory. The script will
find the location of these files and import
them into the database once created