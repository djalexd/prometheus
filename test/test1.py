import sys, time, getch

def main():
	print 'Press a key'


	# main loop -- we just handle input.
	while True:
		ch = getch.getch()
		if ch == 'a':
			print 'going right'
		elif ch == 'd':
			print 'going left'
		elif ch == 'w':
			print 'forward!'
		elif ch == 's':
			print 'brake..'
		else:
			# reset all values (both pwm and dir)
			print 'reseting everything'

		# sleeping for 1s ... hmm that's long
		time.sleep(0.05)


# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
	main()