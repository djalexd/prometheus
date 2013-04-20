""" Simulate a physical environment """
from mock import *
import unittest
import time

from vector_math import *
from car_brain import *
from environment import *
from behavior import *

import logging
logging.basicConfig(format='%(asctime)s %(levelname)s: %(message)s', filename='example.log', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.DEBUG)

# mock = Mock()
# with patch.dict('sys.modules', {'RPIO': mock, 'RPi': mock, 'spidev': mock}):

class SimpleEnvironmentsTest(unittest.TestCase):

	def test_should_not_hit_walls_simplest_room(self):
		# when
		_c = SimulationCar("jsons/car-config.json")
		_e = SimulationEnvironment("jsons/simplest-square.json")

		_c.place_in_environment(Point2d(20, 20), 0)
		_s = SimulationSensor(25, 150, _c, _e)

		brain = CarBrain(_c, _s, SteerForDurationBehavior())
		# then -- we don't do anything
		# assert -- let's pause this thread for 1 minute
		time.sleep(120)