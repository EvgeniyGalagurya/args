def avg(*etc: int | float) ->int | float:
    '''Add any number of arguments.

    We add any number of arguments and find their average value.

    Args:
        int or float

    Returns:
        Mean value of arguments
    '''
    return sum(etc)/len(etc)
print(avg(1, 3, 5))