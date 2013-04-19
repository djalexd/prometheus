import unittest
from mock import *

class StartStopBehaviorTest(unittest.TestCase):

	# Use a mocked car.
	def setUp(self):

		self.car = car.Car()
		self.car.start = MagicMock()
		self.car.stop = MagicMock()

	def test_start(self):
		# when
		b = behavior.StartStopBehavior(10)
		# then
		b.do_react(15, self.car)
		# start
		assert self.car.start.called

	def test_stop(self):
		# when
		b = behavior.StartStopBehavior(10)
		# then
		b.do_react(9, self.car)
		# start
		assert self.car.stop.called

	def test_stop_then_start(self):
		# when
		b = behavior.StartStopBehavior(10)
		b.do_react(5, self.car)
		# then -- simulate the distance again.
		b.do_react(15, self.car)
		# start
		assert self.car.start.called

# Bootstrap for main
if __name__ == '__main__':
	# Mock hardware python bindings.
	mock = Mock()
	with patch.dict('sys.modules', {'RPIO': mock, 'RPi': mock, 'spidev': mock}):
		import behavior
		import car
		suite = unittest.TestLoader().loadTestsFromTestCase(StartStopBehaviorTest)
		unittest.TextTestRunner(verbosity=2).run(suite)