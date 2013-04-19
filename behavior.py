""" No need to import any specific car class.  """


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
