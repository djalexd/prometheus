
import gpioutils

# Car class.
class Car:

	# Override the default settings
	def __init__(self, front_direction_pin, front_power_pin, rear_direction_pin, rear_power_pin, d2_pin):
		self.motor_d2 = d2_pin
		self.front_pwr = front_power_pin
		self.front_dir = front_direction_pin
		self.back_pwm = rear_power_pin
		self.back_dir = rear_direction_pin
		self.configure()

	# Default pins
	def __init__(self):
		motor_d2  = 11   # d2 is motor driver's way to enable/disable both motors -- we'll set this to high for normal ops
		front_pwr = 18   # pin used to power the front motor
		front_dir = 15   # pin used to control front motor direction (right/left)
		back_pwm  = 12   # pin used to control back motor PWM
		back_dir  = 16   # pin used to control back motor direction (forward/backward)		
		self.configure()

	# Configure gpio pins as output
	def configure(self):
		setup_pins([ self.motor_d2, self.front_pwr, self.front_dir, self.back_pwm, self.back_dir ])
		self.enable()

	# Disable both motors
	def disable(self):
		disable_pin(self.motor_d2)

	def enable(self):
		enable_pin(self.motor_d2)

	# Steer the front wheels to the left
	def steer_left(self):
		enable_pin(self.front_dir)
		enable_pin(self.front_pwd)

	# Steer the front wheels to the right
	def steer_right(self):
		disable_pin(self.front_dir)
		enable_pin(self.front_pwd)

	# Move the car forward
	def go_forward(self):
		enable_pin(self.back_pwm)
		enable_pin(self.back_dir)

	# Move the car backward
	def go_backward(self):
		disable_pin(self.back_pwm)
		enable_pin(self.back_dir)