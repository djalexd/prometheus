
from car import Car
from sensors import DistanceSensor
import threading
import time


class CarBrain(threading.Thread):

	def __init__(self, car, sensor, behavior):
		self.car = car
		self.sensor = sensor
		self.behavior = behavior
		# Start the thread when built.
		self.start()

	def run(self):
		dist = self.sensor.distance_cm()

		# Call do_react for behavior, according to distance
		# upfront.
		self.behavior.do_react(dist, self.car)

		# sleep for 0.1s
		time.sleep(0.1)