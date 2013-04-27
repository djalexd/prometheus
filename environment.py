
from vector_math import *
import json
import math
import logging

ray_length = 10000000

class SimulationEnvironment:
	def __init__(self, file):
		f1 = open(file)
		_json = json.load(f1)

		# Read the maze walls and make sure there's no intersection.
		self.walls = self._convert_json_to_walls(_json["walls"])
			
		#self.objects = json_data["inside_objects"]
		f1.close()

	def __ensure_non_intersecting_walls(self):
		""" Makes sure no walls intersect with each other """
		print 'some'


	def _convert_json_to_walls(self, walls_json):
		_walls = []
		for w in walls_json:
			_walls.append( Vector2d( Point2d(w["x1"], w["y1"] ), Point2d(w["x2"], w["y2"]) ) )
		return _walls

	# def __convert_json_to_objects(self, objects_json):
	# 	_objects = []
	# 	for o in objects_json:
	# 		_objects.

class SimulationCar:
	""" 
		Create a simple car that mimics a physical environment.
	"""
	mult = 4

	def __init__(self, file):

		f1 = open(file)
		_json = json.load(f1)

		self.dimension = _json["dimension"]
		self.steer_angle = _json["steer_angle"]
		self._inv_tan_steer_angle = math.tan(self.steer_angle)
		self.reset_motors()

		f1.close()

	def place_in_environment(self, position, direction_angle):
		self.position = position
		self.direction_angle = direction_angle


	def reset_motors(self):
		self.v = 0
		self.angle = 0

	def stop(self):
		self.v = 0
		self.angle = 0

	def start(self):
		self.angle = 0
		self.v = 2 * self.mult

	def steer_none(self):
		logging.debug('steer_none')
		self.angle = 0

	def steer_left(self):
		logging.debug('steer_left')
		self.angle = -self.steer_angle

	def steer_right(self):
		logging.debug('steer_right')
		self.angle = self.steer_angle

	def go_forward(self):
		self.v = 2 * self.mult

	def go_backward(self):
		self.v = -2 * self.mult

	def set_rate(self, attempt_rate):
		self.v = attempt_rate * self.mult

	def set_speed(self, attempt_rate):
		self.set_rate(attempt_rate)

	def update_after_time(self, elapsed):
		dp = Point2d(elapsed * self.v * math.cos(self.direction_angle), elapsed * self.v * math.sin(self.direction_angle))

		self.position.add(dp)

		# Only update angle if necessary
		A = (self.v * elapsed)**2
		R = (self.dimension * self._inv_tan_steer_angle)**2
		if self.angle > 0:
			self.direction_angle += math.acos( (1 - 0.5 * A / R ) ) 
		elif self.angle < 0:
			self.direction_angle -= math.acos( (1 - 0.5 * A / R ) ) 


		logging.debug("%s - angle = %s, " % (self.position, self.direction_angle) )


class SimulationSensor:
	def __init__(self, min_distance, max_distance, car, environment):
		self.min_distance = min_distance
		self.max_distance = max_distance
		# Used to get direction
		self.car = car
		# Used to get obstacles ahead.
		self.environment = environment

	def distance_cm(self):
		""" Mimic the sensor defined in sensors.py """

		ex = self.car.position.x + ray_length * math.cos(self.car.direction_angle)
		ey = self.car.position.y + ray_length * math.sin(self.car.direction_angle)
		ahead_v = Vector2d(self.car.position, Point2d(ex, ey))

		# lambda function used to filter
		def is_wall_ahead(x): return not math.isinf(ahead_v.distance_to(x))

		# Get only the walls that are ahead
		candidate_walls = filter(is_wall_ahead, self.environment.walls)
		logging.debug('Selected %s Candidates from %s' % (str(candidate_walls), str(self.environment.walls)) )

		# map them to an array of distances
		def df(x): return ahead_v.distance_to(x)
		distances = map(df, candidate_walls)

		# and reduce to the closest distance.
		def minf(x,y): return x if x < y else y
		dist_to_closest_wall = reduce(minf, distances)

		if dist_to_closest_wall < self.min_distance:
			return self.min_distance
		elif dist_to_closest_wall > self.max_distance:
			return self.max_distance
		else:
			return dist_to_closest_wall