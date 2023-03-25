# The volume of a sphere is V = 4/3 πr**3
# Write a function that returns the volume of a sphere given the radius

# To do this, we will need to make use of the number π but you must first import the math module

import math

math.pi

def volume(r):
	"""Returns the volume of a sphere with radius r."""
	v = (4.0/3.0) * math.pi * r**3
	return v

answer = volume(2)
print(answer)


#Write a function that computes the area of a triangle - 1/2 b*h

def triangle_area(b, h):
	"""Calculates the area of a triangle"""
	a = (0.5) * b * h
	return a

new_area = triangle_area(2, 3)
print(new_area)
