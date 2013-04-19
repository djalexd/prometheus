from mock import *
import unittest

mock = Mock()
with patch.dict('sys.modules', {'RPIO': mock, 'RPi': mock, 'spidev': mock}):

	import behavior

	# Use a mocked car. Python loose-type arguments are really cool
	class StubCar:
		# All methods are mocks
		def start(self):
			""" Mock for Car::start """
		def stop(self):
			""" Mock for Car::stop """
		def steer_left(self):
			""" Mock for Car::steer_left """
		def steer_right(self):
			""" Mock for Car::steer_right """
		def steer_none(self):
			""" Mock for Car::steer_none """
		def set_speed(self, v):
			""" Mock for Car::set_speed """

	class StartStopBehaviorTest(unittest.TestCase):

		# Use a mocked car.
		def setUp(self):
			_car = StubCar()
			_car = MagicMock()
			self.car = _car
			self.behavior = behavior.StartStopBehavior(10)

		def test_start(self):
			# when
			# then
			self.behavior.do_react(15, self.car)
			# start
			assert self.car.start.called

		def test_stop(self):
			# when
			# then
			self.behavior.do_react(9, self.car)
			# start
			assert self.car.stop.called

		def test_stop_then_start(self):
			# when
			self.behavior.do_react(5, self.car)
			# then -- simulate the distance again.
			self.behavior.do_react(15, self.car)
			# start
			assert self.car.start.called


	class SteerBehaviorTest(unittest.TestCase):

		# Use a mocked car.
		def setUp(self):
			_car = StubCar()
			_car = MagicMock()
			self.car = _car
			self.behavior = behavior.SteerBehavior(10)

		def test_start(self):
			# when
			# then
			self.behavior.do_react(15, self.car)
			# start
			assert self.car.steer_none.called

		def test_should_decelerate_when_obstacle(self):
			# when
			# then
			self.behavior.do_react(9, self.car)
			# start
			self.car.set_speed.assert_called_once_with(1)

		def test_should_steer_when_obstacle(self):
			# when
			# then
			self.behavior.do_react(5, self.car)
			# assert
			assert self.car.steer_left.called