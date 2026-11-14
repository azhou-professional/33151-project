import math


def launch_ball_spaceship(artificial_gravity_acceleration, initial_velocity, initial_angle, spaceship_radius):
    """
    This simulates one launch of an object in artificial gravity.

    Inputs:
    - Gravitational acceleration (g)
    - Initial velocity (v)
    - Initial angle (theta)
    - Spaceship radius (R)

    Outputs:
    - Distance traveled (d) <measured as straight line distance>
    - Maximum height (h) <measured as distance from floor>
    - Airtime (T)
    - Launch_angle_change (alpha) <measured as angle between final and initial position of launch point>
    - Object_angle_change (beta) <measured as angle between final and initial position of the object>
    """

    dt = 0.001

    t = 0.0
    x = 0.0
    y = -1 * spaceship_radius

    v = initial_velocity
    theta = initial_angle
    v_x = v * math.cos(theta)
    v_y = v * math.sin(theta)

    R = spaceship_radius

    alpha = 0.0
    beta = 0.0

    omega = (artificial_gravity_acceleration / R)**0.5
    # There should be zero acceleration

    max_h = 0.0 # Distance from edge of the spaceship
    
    while (x**2 + y**2) <= R**2: # While it hasn't returned to the "floor"
        t += dt
        x += v_x * dt
        y += v_y * dt

        r = (x**2 + y**2)**0.5

        h = R - r
        if h > max_h:
            max_h = h
    
    d = (x**2 + (R + y)**2)**0.5
    alpha = omega * t
    angle = math.asin(d / (2 * (x**2 + y**2)**0.5))
    if angle < 0:
        angle += math.pi
    beta = 2 * angle

    #print(x, y)
        
    return d, max_h, t, alpha, beta
