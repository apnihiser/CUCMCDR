from app import app, models, forms, Config
from flask import render_template, flash, request
from flask_security import Security, SQLAlchemyUserDatastore, login_required
from flask_login import current_user

# Setup Flask-Security
user_datastore = SQLAlchemyUserDatastore(models.db, models.User, models.Role)
security = Security(app, user_datastore,login_form=forms.ExtendedLoginForm)

# Create a user to test with
#@app.before_first_request
#def create_user():
#    models.db.create_all()
#    user_datastore.create_user(name='<name>', password='<password>')
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
    if current_user.is_authenticated:
        user_id = current_user.get_id()
        user_name = models.User.query.filter_by(id=user_id).first()
        return render_template('index.html',
                               title='Certify_CDR Reporting',
                               user_name=user_name.name)
    else:
        return render_template('index.html',
                               title='Certify_CDR Reporting',
                               user_name='Guest')

@app.route('/cdr', methods=['GET', 'POST'])
@login_required
def cdr():
    if current_user.is_authenticated:
        user_id = current_user.get_id()
        user_name = models.User.query.filter_by(id=user_id).first()
        return render_template("cdr.html",
                               title="CDR Query Page",
                               advancedCallInfo=Config.advancedCallInfo,
                               protocolInfo=Config.protocolInfo,
                               user_name=user_name.name)
    else:
        return render_template("cdr.html",
                               title="CDR Query Page",
                               advancedCallInfo=Config.advancedCallInfo,
                               protocolInfo=Config.protocolInfo,
                               user_name='Guest')

@app.route('/results', methods=['GET', 'POST'])
@login_required
def results():
    args = []
    from_date = request.form['dateTimeOrigination']
    end_date = request.form['edateTimeOrigination']
    calling_num = request.form['callingPartyNumber']
    called_num = request.form['originalCalledPartyNumber']

    colDispFormResults = {
        "_sa_instance_state": "0",
        "authCodeDescription": "0",
        "authorizationCodeValue": "0",
        "authorizationLevel": "0",
        "calledPartyPatternUsage": "0",
        "callingPartyNumber_uri": "0",
        "callingPartyNumberPartition": "0",
        "callSecuredStatus": "0",
        "cdrRecordType": "0",
        "clientMatterCode": "0",
        "comment": "0",
        "currentRoutingReason": "0",
        "destCallTerminationOnBehalfOf": "0",
        "destCause_location": "0",
        "destCause_value": "0",
        "destConversationId": "0",
        "destDeviceName": "0",
        "destDTMFMethod": "0",
        "destIpAddr": "0",
        "destIpv4v6Addr": "0",
        "destLegIdentifier": "0",
        "destMediaCap_Bandwidth": "0",
        "destMediaCap_g723BitRate": "0",
        "destMediaCap_maxFramesPerPacket": "0",
        "destMediaCap_payloadCapability": "0",
        "destMediaTransportAddress_IP": "0",
        "destMediaTransportAddress_Port": "0",
        "destMobileCallDuration": "0",
        "destMobileDeviceName": "0",
        "destNodeId": "0",
        "destPrecedenceLevel": "0",
        "destRSVPAudioStat": "0",
        "destRSVPVideoStat": "0",
        "destSpan": "0",
        "destVideoCap_Bandwidth": "0",
        "destVideoCap_Bandwidth_Channel2": "0",
        "destVideoCap_Codec": "0",
        "destVideoCap_Codec_Channel2": "0",
        "destVideoCap_Resolution": "0",
        "destVideoCap_Resolution_Channel2": "0",
        "destVideoChannel_Role_Channel2": "0",
        "destVideoTransportAddress_IP": "0",
        "destVideoTransportAddress_IP_Channel2": "0",
        "destVideoTransportAddress_Port": "0",
        "destVideoTransportAddress_Port_Channel2": "0",
        "finalCalledPartyNumber_uri": "0",
        "finalCalledPartyNumberPartition": "0",
        "finalCalledPartyPattern": "0",
        "finalMobileCalledPartyNumber": "0",
        "globalCallID_callId": "0",
        "globalCallID_callManagerId": "0",
        "globalCallId_ClusterID": "0",
        "huntPilotDN": "0",
        "huntPilotPartition": "0",
        "huntPilotPattern": "0",
        "IncomingICID": "0",
        "IncomingOrigIOI": "0",
        "IncomingProtocolCallRef": "0",
        "IncomingProtocolID": "0",
        "IncomingTermIOI": "0",
        "joinOnBehalfOf": "0",
        "lastRedirectDn": "0",
        "lastRedirectDn_uri": "0",
        "lastRedirectDnPartition": "0",
        "lastRedirectingPartyPattern": "0",
        "lastRedirectingRoutingReason": "0",
        "lastRedirectRedirectOnBehalfOf": "0",
        "lastRedirectRedirectReason": "0",
        "mobileCallingPartyNumber": "0",
        "mobileCallType": "0",
        "origCalledPartyRedirectOnBehalfOf": "0",
        "origCalledPartyRedirectReason": "0",
        "origCallTerminationOnBehalfOf": "0",
        "origCause_location": "0",
        "origCause_value": "0",
        "origConversationId": "0",
        "origDeviceName": "0",
        "origDTMFMethod": "0",
        "originalCalledPartyNumber_uri": "0",
        "originalCalledPartyNumberPartition": "0",
        "originalCalledPartyPattern": "0",
        "origIpAddr": "0",
        "origIpv4v6Addr": "0",
        "origLegCallIdentifier": "0",
        "origMediaCap_Bandwidth": "0",
        "origMediaCap_g723BitRate": "0",
        "origMediaCap_maxFramesPerPacket": "0",
        "origMediaCap_payloadCapability": "0",
        "origMediaTransportAddress_IP": "0",
        "origMediaTransportAddress_Port": "0",
        "origMobileCallDuration": "0",
        "origMobileDeviceName": "0",
        "origNodeId": "0",
        "origPrecedenceLevel": "0",
        "origRoutingReason": "0",
        "origRSVPAudioStat": "0",
        "origRSVPVideoStat": "0",
        "origSpan": "0",
        "origVideoCap_Bandwidth": "0",
        "origVideoCap_Bandwidth_Channel2": "0",
        "origVideoCap_Codec": "0",
        "origVideoCap_Codec_Channel2": "0",
        "origVideoCap_Resolution": "0",
        "origVideoCap_Resolution_Channel2": "0",
        "origVideoChannel_Role_Channel2": "0",
        "origVideoTransportAddress_IP": "0",
        "origVideoTransportAddress_IP_Channel2": "0",
        "origVideoTransportAddress_Port": "0",
        "origVideoTransportAddress_Port_Channel2": "0",
        "OutgoingICID": "0",
        "OutgoingOrigIOI": "0",
        "OutgoingProtocolCallRef": "0",
        "OutgoingProtocolID": "0",
        "OutgoingTermIOI": "0",
        "outpulsedCalledPartyNumber": "0",
        "outpulsedCallingPartyNumber": "0",
        "outpulsedLastRedirectingNumber": "0",
        "outpulsedOriginalCalledPartyNumber": "0",
        "pkid": "0",
        "totalWaitTimeInQueue": "0",
        "wasCallQueued": "0"
    }

    # generate a list from boolean forms to send to the results output
    for key in request.form.keys():
        for value in request.form.getlist(key):
            if key[:5] == 'disp_':
                colDispFormResults.pop(value)
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

    if current_user.is_authenticated:
        user_id = current_user.get_id()
        user_name = models.User.query.filter_by(id=user_id).first()
        return render_template('results.html',title='Requested CDR Records',results=results,user_name=user_name.name)
