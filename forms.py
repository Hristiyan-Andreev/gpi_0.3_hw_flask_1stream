from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField, FormField, HiddenField
from wtforms.validators import DataRequired

# Form for setting Elemental Live IP address
class IPForm(FlaskForm):
	ipaddress = StringField('Elemental IP Adress', validators=[DataRequired()] )
	submit = SubmitField('Set')

# Form for setting Elemental streamID to an GPIO input
class GPItoID(FlaskForm):	
	stream_id = IntegerField('Stream ID:', validators=[DataRequired()] )
	setbut = SubmitField('Set', validators=[DataRequired()])


# Buttons for manual Testing of GPI signal, activating or logging GPI inputs
class GPIctrl(FlaskForm):
	gpi_id = FormField(GPItoID)
	testbut = SubmitField('Test')