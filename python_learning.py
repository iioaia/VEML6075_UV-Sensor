##  Test stuff in Python ##
import time
from time import sleep
import unicornhathd
import veml6075
import smbus

bus = smbus.SMBus(1)

uhat = unicornhathd

uvsensor = veml6075.VEML6075(i2c_dev=bus)
uvsensor.set_shutdown(False)
uvsensor.set_high_dynamic_range(False)
uvsensor.set_integration_time('100ms')

uhat.brightness(0.05)




def leds():
	uhat.set_pixel(5, 0, 0, 0, 244)
	print "Pixel set 0, 0. top Corner"
	uhat.set_pixel(5, 15, 0, 240, 0)
	print "Pixel set to 15, 15  or  16,16, opposite corner"
	sleep(1)
	
def sensors():
	uva, uvb = uvsensor.get_measurements()
	uv_comp1, uv_comp2 = uvsensor.get_comparitor_readings()
	uv_indices = uvsensor.convert_to_index(uva, uvb, uv_comp1, uv_comp2)
	print('UVA : {0} UVB : {1} COMP 1 : {2} COMP 2 : {3}'.format(uva, uvb, uv_comp1, uv_comp2))
	print ('UVA INDEX: {0[0]} UVB INDEX : {0[1]} AVG UV INDEX : {0[2]}\n'.format(uv_indices))
	time.sleep(2)

	



running = True
try:
	while running:
		leds()
		uhat.show()
		sleep(5)
		sensors()
		sleep(200)
		
		


except KeyboardInterrupt:
	unicornhathd.off()
