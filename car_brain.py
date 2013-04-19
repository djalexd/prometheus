import threading
import time
import logging

class CarBrain(threading.Thread):
	""" Wire the car, sensor and behavior. """
	def __init__(self, car, sensor, behavior):

		super(CarBrain, self).__init__()

		self.car = car
		self.sensor = sensor
		self.behavior = behavior
		# Start the (daemon) thread when built.
		self.daemon = True
		self.start()

	def run(self):

		while True:

			dist = self.sensor.distance_cm()
			logging.debug('Read distance %d' % dist)

			# Call do_react for behavior, according to distance
			# upfront.
			self.behavior.do_react(dist, self.car)

			# sleep for 0.1s
			time.sleep(0.1)

			# possibly update the car. This is nothing more but a hook to
			# update its internal state, according to the elapsed time, etc.
			self.car.update_after_time(0.1)