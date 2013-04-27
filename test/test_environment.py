from environment import *
from vector_math import *
import unittest
import math

class SimulationSensorTests(unittest.TestCase):

	def setUp(self):
		self.car = SimulationCar("test/test-car-config.json")
		self.env = SimulationEnvironment("test/test-walls.json")
		self.sensor = SimulationSensor(20, 50, self.car, self.env)

	def test_should_read_max_sensor_distance_when_no_abstacles_ahead(self):
		# when
		self.car.place_in_environment(Point2d(200, 200), 1.78)
		# then
		dist = self.sensor.distance_cm()
		# assert
		assert dist == 50.0
		

	def test_should_read_min_sensor_distance_when_obstacle_too_close(self):
		# when
		self.car.place_in_environment(Point2d(390, 50), 0)
		# then
		dist = self.sensor.distance_cm()
		# assert
		assert dist == 20.0

	def test_should_read_correct_distance_when_obstacle_in_range(self):
		# when
		self.car.place_in_environment(Point2d(360, 50), 0)
		# then
		dist = self.sensor.distance_cm()
		# assert
		assert dist == 40.0

	def test_should_read_correct_distance_when_obstacle_in_range_angle1(self):
		# when
		self.car.place_in_environment(Point2d(380, 50), math.pi / 4)
		# then
		dist = self.sensor.distance_cm()
		# assert
		assert math.fabs(dist - 28.284271247) < epsilon
