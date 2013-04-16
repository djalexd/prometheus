
from gpioutils import *
# we use RPIO library to emulate a pwm. This can be done on any port
# but we'll use the hardware one (not sure if this makes any difference);
from RPIO import PWM

# Car class.
class Car:

	# Speeds of back motor.
	servo_rate = 1
	servo_allowed_rates = {
		1 : 2500,
		2 : 5000,
		3 : 7500,
		4 : 10000
	}

	# Used to drive the engine.
	servo = PWM.Servo()

	# Default pins
	# Override the default settings
	def __init__(self, d2_pin = 11, 
				 front_direction_pin = 15, front_power_pin = 18, 
				 rear_direction_pin = 16, rear_power_pin = 12):
	    # d2 is motor driver's way to enable/disable both motors 
	    # -- we'll set this to high for normal ops
		self.motor_d2 = d2_pin
		# pin used to power the front motor
		self.front_pwr = front_power_pin
		# pin used to control front motor direction (right/left)
		self.front_dir = front_direction_pin
		# pin used to control back motor PWM. This pin is converted to
		# BCM format used by RPIO/PWM module -- "As of yet only BCM GPIO numbering is supported."
		self.back_pwm = rear_power_pin
		self.back_pwm_bcm = convert_to_bcm(rear_power_pin)
		# pin used to control back motor direction (forward/backward)		
		self.back_dir = rear_direction_pin
		self.configure()

	# Configure gpio pins as output and set D2 pin to high, along with
	# reseting the pins to motors.
	def configure(self):
		setup_pins([ self.motor_d2, self.front_pwr, self.front_dir, self.back_pwm, self.back_dir ])
		self.enable()
		self.reset_motors()

	# Disable both motors
	def disable(self):
		disable_pin(self.motor_d2)

	def enable(self):
		enable_pin(self.motor_d2)

	def reset_motors(self):
		disable_pins([ self.front_pwr, self.front_dir, self.back_dir ])
		# Disable servo DMA channel
		servo.stop_servo(self.back_pwm_bcm)

	# Steer the front wheels to the left
	def steer_left(self):
		enable_pin(self.front_dir)
		enable_pin(self.front_pwr)

	# Steer the front wheels to the right
	def steer_right(self):
		disable_pin(self.front_dir)
		enable_pin(self.front_pwr)

	# Move the car forward
	def go_forward(self):
		self.set_speed(self.servo_rate)
		disable_pin(self.back_dir)

	# Move the car backward
	def go_backward(self):
		self.set_speed(self.servo_rate)
		enable_pin(self.back_dir)

	# Just sets the rate without starting the engine.
	def set_rate(self, attempt_rate):
		if (self.servo_allowed_rates[attempt_rate] is None)
			raise Exception("Cannot set servo rate to %d -- unknown servo mapping" % attempt_rate)

		self.servo_rate = attempt_rate

	# Try to set a given rate. Will throw exception if
	# allowed_rates doesnt have a mapping.
	def set_speed(self, attempt_rate):
		self.set_rate(attempt_rate)
		
		r = self.servo_allowed_rates[self.servo_rate]
		servo.set_servo(self.back_pwm_bcm, r)
		print 'Set servo rate to %d' % r