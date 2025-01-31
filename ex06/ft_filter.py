def ft_filter(function, iterable):
    """
    Reimplements the built-in filter function.

    Args:
        function: A function that returns True or False.
        iterable: An iterable (list, tuple, etc.) to filter.

    Returns:
        A generator with elements from iterable for which function returns
        True.
    """
    if function is None:
        return (item for item in iterable if item)
    return (item for item in iterable if function(item))
