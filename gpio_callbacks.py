# Raspberry GPIO dependencies
import time
import RPi.GPIO as GPIO

# Config files
import config as cf
# Elemental Live API commands
import liveapi
# Setup GPIO inputs/outputs
	#Use Board pin numbering - etc. (12) in pinout command
GPIO.setmode(GPIO.BOARD)
	#Setup GPI_1 as the input with PULL-UP
GPIO.setup( cf.GPI_1, GPIO.IN, pull_up_down=GPIO.PUD_UP )

# Define callbacks
state = 0
def start_stop_avail(gpi):
	global state
	print("4. Event detcted")
	
	if GPIO.input(gpi):					# Rising edge == True
		if state == 1:
			print("Stopping cue")
			startime = time.time()
			liveapi.cue_command(cf.elemental_ip, cf.gpi2stream[str(gpi)], 'stop_cue')
			print("Reaction time: " + str(time.time() - startime))
			state = 0
			time.sleep(cf.wait_time)
	else:								# Rising edge == False
		if state == 0:
			print("Starting cue")
			startime = time.time()
			liveapi.cue_command(cf.elemental_ip, cf.gpi2stream[str(gpi)], 'start_cue')			
			print("Reaction time: " + str(time.time() - startime))
			state = 1
			time.sleep(cf.wait_time)
