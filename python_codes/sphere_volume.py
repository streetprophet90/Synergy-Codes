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


# Write a keyword function that converts inch and feet to centimeters

def cm(foot=0, inch=0):
	"""Converts feet and inch to cm given inch and/or feet"""
	inch_to_cm = inch * 2.54
	foot_to_cm = foot * 12 * 2.54
	return inch_to_cm + foot_to_cm

# Call the function and convert inch to cm
cm(inch=12)

# call the function and convert feet to cm
cm(foot=2)

# call the function and convert both feet and inches to cm
inch_foot = cm(foot=2, inch = 12)
print(inch_foot)

"""You can use both keyword arguments and required arguments. However, the required
arguments must always come first"""

def fnx(y, x=0): #in this function both required and keyword arguments have been used
	return x+y

fnx(6, x=3)
	
