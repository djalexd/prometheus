""" No need to import any specific car class.  """

import datetime
import random


class StartStopBehavior:
	""" A simple start / stop behavior. Below the min_distance, the car will simply stop. """

	def __init__(self, min_distance = 35):
		self.min_distance = min_distance

	def do_react(self, distance_cm, car):

		if distance_cm < self.min_distance:
			car.stop()
		else:
			car.start()


class SteerBehavior:
	""" A more complex behavior that will attempt to steer the car when sensor reports below
	    a given threshold. """

	def __init__(self, min_distance = 40):
		self.min_distance = min_distance

	def do_react(self, distance_cm, car):
		# Decelerate
		if distance_cm < self.min_distance:
			car.set_speed(1)
			car.steer_left()
		else:
			# If no obstacle present, reset steering.
			car.set_speed(2)
			car.steer_none()


class SteerForDurationBehavior:
	""" A complex behavior that only steers for a duration of time; if an obstacle is still present,
	    stop the car. """

	class SteerStep:
		""" History of steerings """

	# This class has "memory". It holds a list of steering history, along with duration,
	# estimated distance and angle traveled.
	history = []
	is_currently_steering = False
		#print 'Ahead vector %s' % ahead_v
	def __init__(self, start_steer_distance = 70, min_distance = 30, duration = 2.5):
		self.duration = duration
		self.min_distance = min_distance
		self.start_steer_distance = start_steer_distance


		self.last_obstacle_time = 0

	def do_react(self, distance_cm, car):
		# fallback - if we are below min_distance, can't do anything
		if distance_cm < self.min_distance:
			car.stop()
			return

		# if we need to start steering, do it
		if distance_cm < self.start_steer_distance:
			# if we're already steering, do nothing
			if self.is_currently_steering:
				return

			self.is_currently_steering = True
			car.set_speed(1)
			# randomly select a direction. At a later point, after some history
			# we could assert on a better direction (and not pick one randomly);
			dir = random.randint(0, 1)
			if dir == 1:
				# left
				car.steer_left()
			else:
				# right
				car.steer_right()

		else:
			# obstacle cleared, reset the front wheels and accelerate
			car.set_speed(2) 
			car.steer_none()

			self.is_currently_steering = False
