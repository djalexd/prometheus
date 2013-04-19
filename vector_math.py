""" Utilities to work with 2d environments """
import math

# For floating point operations, we need a FP margin
epsilon = 0.0001


class Point2d:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def distanceTo(self, other):
		dx = self.x - other.x
		dy = self.y - other.y
		return math.sqrt(dx * dx + dy * dy)

	# fluent
	def add(self, other):
		self.x += other.x
		self.y += other.y
		return self

	def is_equal_to(self, other):
		""" Checks equality between 2 points; uses epsilon for edge cases """
		return ( math.fabs(self.x - other.x) < epsilon and math.fabs(self.y - other.y) < epsilon)


	def __str__(self):
		return "(%f,%f)" % (self.x, self.y)


class Vector2d:

	def __init__(self, start, end):
		self.start = start
		self.end = end

	# def __init__(self, start, direction, length):
	# 	self.start = start
	# 	self.end = Point2d(start.x + direction.x * length, start.y + direction.y * length)

	def length(self):
		return self.start.distanceTo(self.end)

	def direction(self):
		inv_len = 1.0 / self.length()
		return Point2d( (self.end.x - self.start.x) / inv_len, (self.end.y - self.start.y) / inv_len )

	def is_equal_to(self, other):
		""" Checks equality between 2 vectors; uses epsilon for edge cases """
		return self.start.is_equal_to(other.start) and self.end.is_equal_to(other.end)

	def is_parallel_with(self, other):
		return self.direction().is_equal_to(other.direction())

	def distance_to(self, other):
		if not self.intersects_with(other):
			return float('inf')

		(l1, l2) = self._compute_segments(other)

		return self.length() * l1

	#def intersection_point(self, other):

	def __str__(self):
		return "%s => %s" % (self.start, self.end)

	def __repr__(self):
		return self.__str__()		


	def intersects_with(self, other):
		""" Checks that 2 vectors intersect at some point. 

			Does not return the intersection point, only
			intersection result (true / false). 
		"""
		if self.is_equal_to(other):
			return False;
		if self.is_parallel_with(other):
			return False;

		(l1, l2) = self._compute_segments(other)

		# Don't count epsilon. This ensures that connected
		# vectors are not considered as intersected;
		return l2 >= epsilon and l2 <= 1.0 - epsilon and l1 >= epsilon and  l1 <= 1.0 - epsilon


	def _compute_segments(self, other):
		""" Computes l1, l2 segments (unbound to 0-1 range) that can be used
			to determine the intersection point. 

			<b>Important</b> this method also checks for non-intersecting 
			vectors and will return (inf, inf) in that case;
		"""

		ax = self.start.x
		ay = self.start.y

		bx = self.end.x
		by = self.end.y

		cx = other.start.x
		cy = other.start.y

		dx = other.end.x
		dy = other.end.y

		_A = (bx - cx)*(cy - ay) - (cx - ax)*(by - ay)
		_B = (dx - cx)*(by - ay) - (bx - ax)*(dy - cy)

		# B is so low we can consider it zero. In that case, l1 and l2 are infinite
		if math.fabs(_B) < epsilon:
			l1 = float('inf')
			l2 = float('inf')
		else:
			l2 = _A / _B
			l1 = ( (cx - ax) + l2 * (dx - cx) ) / (bx - ax)

		return (l1, l2)