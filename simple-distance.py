import time
import mcp3008

def main():

	while True:
		r = []
		for i in range (0,10):
			r.append(mcp3008.readadc(1))
		a = sum(r)/10.0
		v = (a/1023.0)*3.3
		d = 16.2537 * v**4 - 129.893 * v**3 + 382.268 * v**2 - 512.611 * v + 306.439
		cm = int(round(d))
		print '%d cm' % cm
		time.sleep(1)

# Standard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
	main()

