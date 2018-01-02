from flask_security.forms import LoginForm
from wtforms import StringField
from wtforms.validators import InputRequired

class ExtendedLoginForm(LoginForm):
    email = StringField('Username', [InputRequired()])
