from flask_wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired

class QueryForm(Form):
    called = StringField('called')
    calling = StringField('calling')
    fromdate = StringField('fromdate')
    todate = StringField('todate')
    dc_callingPartyNumber = BooleanField('callingPartyNumber', default=True)
    dc_originalCalledPartyNumber = BooleanField('originalCalledPartyNumber', default=True)