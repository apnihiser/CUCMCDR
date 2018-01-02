from app import app, models, forms
from flask import render_template, flash, redirect, request, url_for
from flask_security import Security, SQLAlchemyUserDatastore, login_required

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(models.db, models.User, models.Role)
security = Security(app, user_datastore,login_form=forms.ExtendedLoginForm)

# Create a user to test with
#@app.before_first_request
#def create_user():
#    models.db.create_all()
#    user_datastore.create_user(name='IVCAteam', password='<create a password>')
#    models.db.session.commit()

@app.errorhandler(401)
def auth_error():
    return render_template("401.html")

@app.errorhandler(404)
def page_not_found():
    return render_template("404.html")

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Certify_CDR Reporting')

@app.route('/cdr', methods=['GET', 'POST'])
@login_required
def cdr():
    return render_template("cdr.html", title="CDR Query Page")

@app.route('/results', methods=['GET', 'POST'])
@login_required
def results():

    # Goal - return a query which returns a descriptive header, with results provided below
    # each column should be specified by the query page
    # dynamic parameters that allow all parameters, no parameters, and a mix of any.
    # ex. calling number 1940 during 2/1/17 and 2/28/17 (check marked to return called numbers only
    # would return all called numbers column from 1940 during the date range provided.
    # col1 col2 col3
    # 1    2    3
    #----------------------------------------------------------------------------------------------
    # args list needs to be generated dynamically to fill out the query statement.
    # example
    # args = [
    #     models.CDR.dateTimeOrigination >= 1511189950,
    #     models.CDR.dateTimeOrigination <= 1511190006,
    #     models.CDR.callingPartyNumber == 1530
    # ]

    args = []
    colDispFormResults = ['_sa_instance_state',]
    from_date = request.form['dateTimeOrigination']
    end_date = request.form['edateTimeOrigination']
    calling_num = request.form['callingPartyNumber']
    called_num = request.form['originalCalledPartyNumber']

    # generate a list from boolean forms to send to the results output
    for key in request.form.keys():
        for value in request.form.getlist(key):
            if key[:5] == 'disp_':
                colDispFormResults.append(value)
    # incoming POST no entries return entire db
    if request.method == 'POST' and from_date == '' and end_date == '' and calling_num == '' and called_num == '':
        # general query statement
        q = models.CDR.query.all()
    # incoming POST date range data from cdr.html
    elif request.method == 'POST' and (from_date != '' or end_date != '' or calling_num != '' or called_num != ''):
        if from_date != '':
            args.append(models.CDR.dateTimeOrigination >= from_date)
        if end_date != '':
            args.append(models.CDR.dateTimeOrigination <= end_date)
        if calling_num != '':
            args.append(models.CDR.callingPartyNumber == calling_num)
        if called_num != '':
            args.append(models.CDR.originalCalledPartyNumber == called_num)
        # general query statement
        q = models.CDR.query.filter(*args).all()
    else:
        flash('Something went wrong somewhere! Please check with Telephony Administration.')
        return render_template('cdr.html',title='CDR Query Error')

    # generate a list of dictionaries
    results = [item.__dict__ for item in q]
    # modify the SQL query object to trim columns to user specification
    for result in results:
        for columnName in colDispFormResults:
            result.pop(columnName, None)
    if results == []:
        flash('No records found from that search.')
    # send query result to the result.html page to be rendered
    return render_template('results.html',title='Requested CDR Records',results=results)