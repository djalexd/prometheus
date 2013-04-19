from vector_math import *
import unittest

class Point2dTests:
	
	def test_add_should_work(self):
		# when
		p1 = Point2d(5, 3)
		# then
		p1.add(Point2d(1, 9))
		# assert
		assert p1.x == 6
		assert p1.y == 12


class Vector2dTests(unittest.TestCase):

	def test_intersects_between_parallel_vectors(self):
		# when
		v1 = Vector2d(Point2d(5, 10), Point2d(15, 10))
		v2 = Vector2d(Point2d(0, 0), Point2d(10, 0))
		# then
		# assert
		assert v1.intersects_with(v2) is False

	def test_distance_between_parallel_vectors(self):
		# when
		v1 = Vector2d(Point2d(20, 20), Point2d(10000020, 20))
		v2 = Vector2d(Point2d(0, 0), Point2d(10000, 0))
		# then
		# assert
		assert v1.distance_to(v2) == float('inf')

	def test_distance_between_vector_behind(self):
		# when
		v1 = Vector2d(Point2d(20, 20), Point2d(10000020, 20))
		v2 = Vector2d(Point2d(0, 10000), Point2d(0, 0))
		v3 = Vector2d(Point2d(10000, 0), Point2d(10000, 10000))
		# then
		#assert
		assert v1.distance_to(v2) == float('inf')