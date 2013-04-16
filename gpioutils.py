
# gpio is strict import here.
import RPi.GPIO as gpio

# Utility methods for gpio.

# Enable a preconfigured pin. 
def enable_pin(pin):
	gpio.output(pin, gpio.HIGH)

# Disable a preconfigured pin.
def disable_pin(pin):
	gpio.output(pin, gpio.LOW)

# Enable a list of pins.
def enable_pins(pins_list):
	for pin in pins_list:
		try:
			enable_pin(pin)
		except Exception:
			# We just handle all exception types here, because we're inside a loop
			print 'Unable to enable pin %d' % pin

# Disable a list of pins.
def disable_pins(pins_list):
	for pin in pins_list:
		try:
			disable_pin(pin)
		except Exception:
			# We just handle all exception types here, because we're inside a loop
			print 'Unable to disable pin %d' % pin


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
