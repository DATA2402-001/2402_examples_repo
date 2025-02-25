def calculate_weight(mass: float, g: float = 9.81):
    """
    calculate weight of an object
    param mass: mass of the object in kg
    param g: gravitational acceleration 
    (defaults to 9.81 m/s/s)
    returns: weight in newtons
    """
    return mass * g


# get weight of a 10 kg object
weight = calculate_weight(10)

# get weight of the object on mars (g=3.72)
weight_mars = calculate_weight(10, 3.72)

# supply arguments by name
weight = calculate_weight(g=4.0, mass=10)
