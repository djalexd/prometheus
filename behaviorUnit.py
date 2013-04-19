import unittest
from mock import *

class StartStopBehaviorTest(unittest.TestCase):

	# Use a mocked car.
	def setUp(self):

		car = car.Car()
		car.start = MagicMock()
		car.stop = MagicMock()

		self.car = car
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

		car = car.Car()
		car.start = MagicMock()
		car.stop = MagicMock()
		car.steer_left = MagicMock()
		car.steer_right = MagicMock()
		car.set_speed = MagicMock()

		self.car = car
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
		assert self.car.stop.set_speed.called(1)

	def test_should_steer_when_obstacle(self):
		# when
		# then
		self.behavior.do_react(5, self.car)
		# assert
		assert self.car.steer_left.called

	#def test_stop_then_start(self):
		# when
	#	self.behavior.do_react(5, self.car)
		# then -- simulate the distance again.
	#	self.behavior.do_react(15, self.car)
		# start
	#	assert self.car.start.called


# Bootstrap for main
if __name__ == '__main__':
	# Mock hardware python bindings.
	mock = Mock()
	with patch.dict('sys.modules', {'RPIO': mock, 'RPi': mock, 'spidev': mock}):
		import behavior
		import car

		suite1 = unittest.TestLoader().loadTestsFromTestCase(StartStopBehaviorTest)
		suite2 = unittest.TestLoader().loadTestsFromTestCase(SteerBehaviorTest)
		unittest.TextTestRunner(verbosity=2).run(unittest.TestSuite([suite1, suite2]))