from vector_math import *
import unittest

class Point2dTests(unittest.TestCase):
	
	def test_add_should_work(self):
		# when
		p1 = Point2d(5, 3)
		# then
		p1.add(Point2d(1, 9))
		# assert
		assert p1.x == 6
		assert p1.y == 12


class Vector2dTests(unittest.TestCase):

	# Holder for origin coordinates
	origin = Point2d(0, 0)

	def test_length_horizontal(self):
		# when
		v1 = Vector2d(self.origin, Point2d(15, 0))
		# then
		# assert
		assert v1.length() == 15.0

	def test_length_at_angle(self):
		# when
		v1 = Vector2d(self.origin, Point2d(3, 4))
		# then
		# assert
		assert v1.length() == 5.0

	def test_direction_is_computed_ok(self):
		# when
		v1 = Vector2d(self.origin, Point2d(10, 10))
		# then
		# assert
		assert v1.direction() == Point2d(0.707106781, 0.707106781)

	def test_intersects_with_should_return_false_for_same_vectors(self):
		# when
		v1 = Vector2d(self.origin, Point2d(14, 7))
		# then
		# assert
		assert v1.intersects_with(v1) is False

	def test_intersects_with_should_return_false_for_parallel_vectors(self):
		# when
		v1 = Vector2d(self.origin, Point2d(4, 9))
		# then
		v2 = Vector2d(Point2d(0, 1), Point2d(4, 10))
		# assert
		assert v1.intersects_with(v2) is False

	def test_intersects_with_should_return_false_for_non_intersecting_vectors(self):
		# when
		v1 = Vector2d(self.origin, Point2d(4, 0))
		v2 = Vector2d(Point2d(5, 1), Point2d(3, 0.1))
		# then
		# assert
		assert v1.intersects_with(v2) is False

	def test_intersects_with_ok(self):
		# when
		v1 = Vector2d(self.origin, Point2d(4, 0))
		v2 = Vector2d(Point2d(4, 1), Point2d(3, -1))
		# then
		# assert
		assert v1.intersects_with(v2) is True

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

	def test_distance_intersecting_vectors(self):
		# when
		v1 = Vector2d(self.origin, Point2d(10, 0))
		v2 = Vector2d(Point2d(4, -2), Point2d(4, 2))
		# then
		# assert
		assert v1.distance_to(v2) == 4.0

	def test_distance_start_end_vectors(self):
		# when
		v1 = Vector2d(self.origin, Point2d(2, 0))
		v2 = Vector2d(Point2d(2, 0), Point2d(5, 3))
		# then
		# assert
		assert v1.distance_to(v2) == 2.0

	def test_distance_same_direction_non_intersecting_vectors(self):
		# when
		v1 = Vector2d(self.origin, Point2d(2, 0))
		v2 = Vector2d(Point2d(3, 0), Point2d(10, 0))
		# then
		assert v1.distance_to(v2) == float('inf')
		# assert