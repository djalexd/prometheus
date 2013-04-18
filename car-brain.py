
from car import Car
from sensors import DistanceSensor


class CarBrain:

	def __init__(self, car, sensor):
		self.car = car
		self.sensor = sensor