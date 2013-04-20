#!/usr/bin/python

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep
import cgi
import car
from RPi import GPIO

PORT_NUMBER = 17005

# configure gpio mode
GPIO.setmode(GPIO.BOARD)
_car = car.Car()

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):
	
	#Handler for the GET requests
	def do_GET(self):
		print 'GET %s' % self.path
		if self.path.startswith('/html'):
			f = open(curdir + sep + self.path) 
			self.send_response(200)
			self.end_headers()
			self.wfile.write(f.read())
			f.close()

		else:

			# These are HTTP GET requests that act on the car.
			if self.path == '/start':
				_car.start()
			elif self.path == '/stop':
				_car.stop()
			elif self.path == '/right':
				_car.steer_right()
			elif self.path == '/left':
				_car.steer_left()
			elif self.path == '/none':
				_car.steer_none()
			elif self.path == '/speed2':
				_car.set_speed(2)
			elif self.path == '/speed3':
				_car.set_speed(3)
			elif self.path == '/speed4':
				_car.set_speed(4)

			self.send_response(200)
			self.wfile.write('Command ok')
			
try:
	#Create a web server and define the handler to manage the
	#incoming request
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	#Wait forever for incoming htto requests
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()