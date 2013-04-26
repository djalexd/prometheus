""" Simulate a physical environment """
from mock import *
import unittest
import time

from vector_math import *
from environment import *
from behavior import *

from PyQt4 import QtCore, QtGui
import sys

import logging
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', filename='example.log', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)


class CarBrainWithoutThreading:
	""" A stub of CarBrain class that does not start a thread, 
		but still lapses time for simulation car.
	"""

	# Step time, in seconds (how much time lapses for each iteration)
	step = 0.1

	def __init__(self, car, sensor, behavior):
		self.car = car
		self.sensor = sensor
		self.behavior = behavior

	def run(self, time_in_seconds):

		# Compute number of steps
		num_steps = int(time_in_seconds / self.step)

		for i in range(0, num_steps):
			dist = self.sensor.distance_cm()
			logging.debug('Read distance %d' % dist)

			# Call do_react for behavior, according to distance
			# upfront.
			self.behavior.do_react(dist, self.car)

			# possibly update the car. This is nothing more but a hook to
			# update its internal state, according to the elapsed time, etc.
			self.car.update_after_time(self.step)



class SimpleEnvironmentsTest(unittest.TestCase):

	def test_should_not_hit_walls_simplest_room(self):
		# when
		_c = SimulationCar("jsons/car-config.json")
		_e = SimulationEnvironment("jsons/simplest-square.json")

		_c.place_in_environment(Point2d(20, 20), 0)
		_s = SimulationSensor(25, 150, _c, _e)

		brain = CarBrainWithoutThreading(_c, _s, SteerForDurationBehavior())
		# then -- 
		brain.run(120)
		# assert
		