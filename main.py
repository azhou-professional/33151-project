import planetary_functions
import spaceship_functions
import math
import numpy as np
import matplotlib.pyplot as plt
import sys


"""
Usage:

    python3 main.py
"""

# Fixed launch angle
launch_angle = math.pi / 4 # 45 degree

# Fix gravity
gravity = 10

# Changing velocity

velocities = []

for velocity in range(5, 105, 5):
    velocities.append(velocity)

# Changing spaceship radius

radii = []

for radius in range(10, 110, 10):
    radii.append(radius)


###
# Planetary sim
###

planetary_data = {}

for velocity in velocities:

    d, h, T = planetary_functions.launch_ball_planetary(gravity, velocity, launch_angle)
    
    planetary_data[velocity] = {"d": d,
                                "h": h,
                                "T": T}



###
# Plotting
###

"""
spaceship_data is a stacked dictionary

spaceship_data[RADIUS][VELOCITY][DATA]
"""

spaceship_data = {}
for radius in radii:
    spaceship_data[radius] = {}



for velocity in velocities:
    for radius in radii:

        d, h, T, alpha, beta = spaceship_functions.launch_ball_spaceship(gravity, velocity, launch_angle, radius)

        arcd = beta * radius - alpha * radius

        spaceship_data[radius][velocity] = {
                "d" : d,
                "h" : h,
                "T" : T,
                "arcd" : arcd
                }
        print(radius, velocity)


"""
    x: radius
    y: velocity
    z: dependent variable
"""

fig, [ad, ah, at] = plt.subplots(3, 1, subplot_kw={'projection': '3d'})

for graph in [ad, ah, at]:
    graph.set_xlabel("Station Radius")
    graph.set_ylabel("Launch Velocity")

ad.set_title("Distance traveled by object")
ah.set_title("Maximum height of object")
at.set_title("Airtime")

ad.set_zlabel("Distance")
ah.set_zlabel("Height")
at.set_zlabel("Time")

for velocity in velocities:
    for radius in radii:
        ad.scatter(radius, velocity, planetary_data[velocity]["d"], color="green", label="Planetary", marker="o")
        ah.scatter(radius, velocity, planetary_data[velocity]["h"], color="green", label="Planetary", marker="o")
        at.scatter(radius, velocity, planetary_data[velocity]["T"], color="green", label="Planetary", marker="o")

        ad.scatter(radius, velocity, spaceship_data[radius][velocity]["arcd"], color="blue", label="Space", marker="o")
        ah.scatter(radius, velocity, spaceship_data[radius][velocity]["h"], color="blue", label="Space", marker="o")
        at.scatter(radius, velocity, spaceship_data[radius][velocity]["T"], color="blue", label="Space", marker="o")

plt.show()


