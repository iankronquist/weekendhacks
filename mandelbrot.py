#!/usr/bin/env python

import Image

def main():
	cellsize = 10
	mandelbrot(1000)

def mandelbrot(precision):
	increment = 0.001
	height = 2
	width = 3.5
	img = Image.new( 'RGB', (3500,2000), "black") # create a new black image
	pixels = img.load() # create the pixel map
	img.show()
	for y0 in drange(-1, 1, increment):
		for x0 in drange(-2.5,1, increment):
			x = 0
			y = 0
			iteration = 0
			while x ** 2 + y **2 < 2**2 and iteration < precision:
				xtemp = x ** 2 - y **2 + x0 
				y = 2 * x * y + y0
				x = xtemp
				iteration += 1
				pixels[convertx(x0),converty(y0)] = (iteration,10,100)
		print 'Wrote row: ', y0
        	#if you want to periodically save the picture, uncomment the next line.
		#img.save('mandelbrot.png')
	img.save('mandelbrot.png')
	print 'done\a\a\a\a\a!'
		
def drange(start, stop, step):
	r = start
	while r < stop:
		yield r
		r += step

def convertx(x):
	#print 'initx', x
	x = (x + 2.5) * 1000
	#print 'x', x
	return x

def converty(y):
	#print 'inity', y
	y = (y + 1) * 1000
	#print 'y', y
	return y
	
main()
