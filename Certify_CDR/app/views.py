from app import app, db, models
from flask import render_template, flash, redirect, request, url_for, session, escape
from .forms import QueryForm


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
                           title='Certify_CDR Reporting')

@app.route('/cdr', methods=['GET', 'POST'])
def cdr():
    return render_template("cdr.html",)

@app.route('/results', methods=['GET', 'POST'])
def results():
    error = ''

    if request.method == 'POST':
        called_parameter = request.form['called']
        calling_parameter = request.form['calling']
        fromdate_parameter = request.form['fromdate']
        todate_parameter = request.form['todate']

        #flash(called_parameter)
        #flash(calling_parameter)
        #flash(fromdate_parameter)
        #flash(todate_parameter)

        dateQ = models.CDR.query.filter(models.CDR.dateTimeOrigination >= fromdate_parameter).filter(
            models.CDR.dateTimeOrigination <= todate_parameter)
        dicts = [(row.__dict__) for row in dateQ]
        for dict in dicts:
            del dict['_sa_instance_state']
        return render_template('results.html',
                               title='CDR Results',
                               dicts=dicts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ''
    try:
        if request.method == "POST":
            attempted_username = request.form['username']
            attempted_password = request.form['password']
            flash(attempted_username)
            flash(attempted_password)
            if attempted_username == "admin" and attempted_password == "password":
                return redirect(url_for('cdr'))
            else:
                error = "Invalid credentials. Try Again."
        return render_template("login.html", error=error)
    except Exception as e:
        flash(e)
        return render_template("login.html", error=error)