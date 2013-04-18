#!/usr/bin/python

# import some relevant modules
import sys, time
try:
	import RPi.GPIO as gpio
except ImportError:
	print("Error importing RPi.GPIO; you are either running the script without sudo priviledges, or running the script on a machine that is not Raspberry (the lib is missing nevertheless)")

from car import Car
import string
import getopt


def usage():
	print 'Usage:\n'
	print ' car-diagnostic.py\n'
	print ' car-diagnostic.py tests=...\n'
	print '   where tests can be any combination of \'direction\', \'power\' and \'rates\''


# Provide some diagnostics
def main(argv):

	try:
		opts, args = getopt.getopt(argv, "ht:d", ["help", "tests="])
	except getopt.GetoptError:
		usage()
		sys.exit(2)

	tests = ["direction", "power", "rates"]

	# configure gpio mode
	gpio.setmode(gpio.BOARD)

	for opt, arg in opts:
		if opt in ("-h", "--help"):
			usage()
			sys.exit()
		elif opt in ("-t", "--tests"):
			tests = string.split(arg)

	print 'Running tests %s' % tests

	car = Car()

	if "direction" in tests:
		print '.Diagnostics: motor control & powering'

		print 'steer_left'
		car.steer_left()
		time.sleep(1)

		print 'steer_right'
		car.steer_right()
		time.sleep(1)

		car.reset_motors()

	if "power" in tests:
		print 'go_forward'
		car.go_forward()
		time.sleep(1)

		print 'go_backward'
		car.go_backward()
		time.sleep(1)

		car.reset_motors()

	if "rates" in tests:
		print '.Diagnostics: motor servo rate'

		car.set_speed(2)
		time.sleep(1)

		car.set_speed(3)
		time.sleep(1)

		car.set_speed(4)
		time.sleep(1)

		# Finally reset the motors again.
		car.reset_motors()

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
	main(sys.argv[1:])