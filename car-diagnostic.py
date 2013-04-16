#!/usr/bin/python

# import some relevant modules
import sys, time
try:
	import RPi.GPIO as gpio
except ImportError:
	print("Error importing RPi.GPIO; you are either running the script without sudo priviledges, or running the script on a machine that is not Raspberry (the lib is missing nevertheless)")

from car import Car

# Provide some diagnostics
def main():
	# configure gpio mode
	gpio.setmode(gpio.BOARD)

	car = Car()

	print '.Diagnostics: motor control & powering'

	print 'steer_left'
	car.steer_left()
	time.sleep(1)

	print 'steer_right'
	car.steer_right()
	time.sleep(1)

	print 'go_forward'
	car.go_forward()
	time.sleep(1)

	print 'go_backward'
	car.go_backward()
	time.sleep(1)

	car.reset_motors()

	print '.Diagnostics: motor servo rate'

	car.set_speed(2)
	time.sleep(1)

	car.set_speed(3)
	time.sleep(1)

	car.set_speed(4)
	time.sleep(1)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
	main()
