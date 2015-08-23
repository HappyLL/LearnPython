__author__ = 'Happyli'



def fact(n):
    '''
    Simple factorial function with doctest.

    >>> fact(-1)
    Traceback (most recent call last):
        ...
    ValueError: No
    >>> fact(1)
    1
    >>> fact(5)
    121
    '''

    if n < 0:
        raise ValueError('No')
    if n == 0 or n == 1:
        return 1
    return n*fact(n-1)

if __name__ == '__main__':
    import doctest
    doctest.testmod()
