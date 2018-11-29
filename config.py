import os

class FlaskConfig(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'PERKELE'
	
	
# Configuration parameters - IPs, Inputs, Stream IDs
	#Define GPI_1 as PIN 40 (GPIO 21)
GPI_1 = 40 							# GPIO 21
	#elemental_ip = '37.157.142.3'
elemental_ip = '192.168.2.3'

	#Mapper of GPI inputs to Elemental live streams
gpi2stream = {
		str(GPI_1): '5'
}

	#Time to wait after edge detection
wait_time = 5