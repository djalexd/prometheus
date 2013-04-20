""" Utilities to work with 2d environments """
import math
from numpy import *
import logging

# For floating point operations, we need a FP margin
epsilon = 0.0000001


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
			#logging.debug('%s considered equal to %s -- intersects_with returned false' % (self, other))
			return False
		if self.is_parallel_with(other):
			#logging.debug('%s considered in the same direction as %s -- intersects_with returned false' % (self, other))
			return False

		(l1, l2) = self._compute_segments(other)
		#logging.debug('Computed line segments to (%s, %s)' % (l1, l2))

		if l1 is None:
			return False

		# Don't count epsilon. This ensures that connected
		# vectors are not considered as intersected;
		return l2 >= 0 and l2 <= 1.0 and l1 >= 0 and l1 <= 1.0


	def _compute_segments(self, other):
		""" Computes l1, l2 segments (unbound to 0-1 range) that can be used
			to determine the intersection point. 

			<b>Important</b> this method also checks for non-intersecting 
			vectors and will return (inf, inf) in that case;

			x1 + a*(x2-x1) = x3 + b*(x4-x3)
			y1 + a*(y2-y1) = y3 + b*(y4-y3)

			b * [ (x4-x3)*(y2-y1) - (y4-y3)*(x2-x1) ] = (y3-y1)*(x2-x1) - (x3-x1)*(y2-y1) => b
			a = [ (x3-x1) + b * (x4-x3) ] / (x2-x1) => a
		"""

		(x1, y1) = (self.start.x, self.start.y)
		(x2, y2) = (self.end.x, self.end.y)
		(x3, y3) = (other.start.x, other.start.y)
		(x4, y4) = (other.end.x, other.end.y)

		_D = (x4-x3)*(y2-y1) - (y4-y3)*(x2-x1)
		if math.fabs(_D) < epsilon:
			# parallel lines, cannot intersect
			return (None, None)

			# This could also mean lines are co-linear.

		else:
			b = ((y3-y1)*(x2-x1) - (x3-x1)*(y2-y1)) / _D

			if math.fabs(x2 - x1) < epsilon:
				a = ( (y3-y1) + b*(y4-y3) ) / (y3-y1)
			else:
				a = ( (x3-x1) + b*(x4-x3) ) / (x2-x1)

			return (a, b)