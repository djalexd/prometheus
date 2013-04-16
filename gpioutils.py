
# gpio is strict import here.
import RPi.GPIO as gpio

# Utility methods for gpio.

# Enable a preconfigured pin. 
def enable_pin(pin):
	gpio.output(pin, gpio.HIGH)

# Disable a preconfigured pin.
def disable_pin(pin):
	gpio.output(pin, gpio.LOW)

# Configure gpio pins as output
def setup_pins(pins_list):
	# configure pins - all are output
	for pin in pins_list:
		try:
			gpio.setup(pin, gpio.OUT)
		except gpio.InvalidChannelException:
			# We throw a more detailed error.
			raise gpio.InvalidChannelException("The channel sent is invalid on a Raspberry Pi: %d" % pin)
			
		print 'Configured output pin %d' % pin
