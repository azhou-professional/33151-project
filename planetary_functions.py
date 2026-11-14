import math


def launch_ball_planetary(gravitational_acceleration, initial_velocity, initial_angle):
    """
    This simulates one launch of an object.
    
    Inputs:
    - Gravitational acceleration (g)
    - Initial velocity (v)
    - Initial angle (theta)

    Outputs:
    - Distance traveled (d)
    - Maximum height (h)
    - Airtime (T)
    """


    dt = 0.001
    
    t = 0.0
    x = 0.0
    y = 0.0

    v = initial_velocity
    theta = initial_angle
    v_x = v * math.cos(theta)
    v_y = v * math.sin(theta)
    g = -1 * gravitational_acceleration

    max_y = 0.0

    while y >= 0.0:
        t += dt
        x += v_x * dt
        y += v_y * dt

        v_y += g * dt

        if y > max_y:
            max_y = y

    return x, max_y, t



