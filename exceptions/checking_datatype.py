def process_integer(x: int):
    """
    this function is expecting an int parameter
    raise a TypeError if x is not an integer
    """

    # here's one way that attempts to cast
    try:
        int(x)
    except ValueError:
        raise TypeError("you must pass in an INTEGER argument for x")
    if int(x) != x: # this covers the case where x is float
        raise TypeError("you must pass in an INTEGER argument for x")
    
    # here's another way that tests x's data type directly
    # this is more strict: 1.0 would raise the exception
    if type(x) != int:
        raise TypeError("you must pass in an INTEGER argument for x")


process_integer('5')
process_integer(1)  # this is fine
process_integer(1.0)  # this is fine
process_integer('abc')  # this should be a TypeError
process_integer(1.1)  # this should be a TypeError