# Flask Web App dependencies
from flask import Flask, render_template, request, jsonify
from flask_wtf.csrf import CSRFProtect
from flask_assets import Bundle, Environment
import liveapi
import forms

# Config files
import config as cf

# GPIO handlers
import gpio_callbacks as gp
import RPi.GPIO as GPIO

# Configure the web app
app = Flask(__name__)
app.config.from_object(cf.FlaskConfig)

csrf = CSRFProtect()
csrf.init_app(app)

# Import web app assets - JS, CSS
jsfiles = Bundle('form_ajax.js', output='gen/main.js')
assets = Environment(app)
assets.register('main_js', jsfiles)

# Tie callbacks to events
GPIO.add_event_detect(cf.GPI_1, GPIO.BOTH, callback = gp.start_stop_avail)

# Define the routes for the Flask web app
@app.route('/')
@app.route('/command_center', methods = ['GET', 'POST'])
def index():
	form_gpiCtrl = forms.GPIctrl()
	if request.method == 'GET':					# When the page loads for first time
		return render_template('command_center.html', form = form_gpiCtrl)


state = 0
@app.route('/gpiCtrl', methods = ['POST'])
def gpi_ctrl():
	global state
	form_gpiCtrl = forms.GPIctrl()
	btn = request.form['btn']
	stream = form_gpiCtrl.stream_id.data
	cf.gpi2stream[str(cf.GPI_1)] = stream
	if btn == 'btn_ss_cue':
		if state == 0:
			response = liveapi.cue_command(cf.elemental_ip, str(stream), 'start_cue')
			state = 1
			
		elif state == 1:
			response = liveapi.cue_command(cf.elemental_ip, str(stream), 'stop_cue')
			state = 0
			
		return response
	elif btn == 'btn_set':
		return "Ip set"
		

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
	