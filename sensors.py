
import mcp3008


class DistanceSensor:
	''' 
	Provides a simple wrapper for mcp3008 adc. Returns distance in centimeters,
	from min 15cm to max 150cm.
	'''

	min_distance = 15
	max_distance = 150
	read_count = 10

	def distance_cm(self):
		r = []
		for i in range (0, self.read_count):
			r.append(mcp3008.readadc(1))
		a = sum(r)/10.0
		v = (a/1023.0)*3.3
		d = 16.2537 * v**4 - 129.893 * v**3 + 382.268 * v**2 - 512.611 * v + 306.439
		cm = int(round(d))

		# Clamp to make sure we don't provide false values.
		if cm < self.min_distance:
			cm = self.min_distance
		if cm > self.max_distance:
			cm = self.max_distance

		return cm