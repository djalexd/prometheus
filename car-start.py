#!/usr/bin/python

# import some relevant modules
import sys, time
try:
	import RPi.GPIO as gpio
except ImportError:
	print("Error importing RPi.GPIO; you are either running the script without sudo priviledges, or running the script on a machine that is not Raspberry (the lib is missing nevertheless)")

# Set some constants; The most important ones are pin numbers
pi        = 3.14 # totally useless, but fun
motor_d2  = 11   # d2 is motor driver's way to enable/disable both motors -- we'll set this to high for normal ops
front_pwr = 17   # pin used to power the front motor
front_dir = 19   # pin used to control front motor direction (right/left)
back_pwm  = 12   # pin used to control back motor PWM
back_dir  = 13   # pin used to control back motor direction (forward/backward)

pins_list = [ motor_d2, front_pwr, front_dir, back_pwm, back_dir ]

def main():
	print 'Starting Raspberry motor input pins'
	# configure gpio mode
	gpio.setmode(gpio.BOARD)
	# configure pins - all are output
	for pin in pins_list:
		try:
			gpio.setup(pin, gpio.OUT)
		except gpio.InvalidChannelException:
			# We throw a more detailed error.
			raise gpio.InvalidChannelException("The channel sent is invalid on a Raspberry Pi: " + pin)

	print 'Finished configuring Raspberry motor pins'

	# main loop -- we just handle input.
	while True:
		str = raw_input();
		if str == "a":
			print 'going right'
		elif str == "d":
			print 'going left'
		elif str == "w":
			print 'forward!'
		elif str == "s":
			print 'brake..'

		# sleeping for 1s ... hmm that's long
		time.sleep(1)


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
	main()
