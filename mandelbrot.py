#!/usr/bin/env python

import Image

def main():
	cellsize = 10
	mandelbrot(1000, 2)

def mandelbrot(precision, size):
	assert size < 5
	size = 10 ** size
	increment = 1.0/float(size) /10
	height = 2
	width = 3.5
	img = Image.new( 'RGB', (35*size,20*size), "black") # create a new black image
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
				pixels[convertx(x0, size),converty(y0, size)] = (iteration,10,100)
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

def convertx(x, size):
	#print 'initx', x
	x = (x + 2.5) * size * 10
	#print 'x', x
	return x

def converty(y, size):
	#print 'inity', y
	y = (y + 1) * size * 10
	#print 'y', y
	return y
	
main()
