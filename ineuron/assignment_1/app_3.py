"""
Write a Python program to find the volume of a sphere with diameter 12 cm.
Formula: V=4/3 * π * r^3
"""
import math

diameter = 12
r = diameter/2

volume_of_sphere = 4 / 3 * math.pi * r ** 3

print(f"Volume of Sphere: {volume_of_sphere}")