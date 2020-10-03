# coding = utf-8
# auteur = Ewan GRIGNOUX LEVERT
# date = Octobre 2020

import doctest
import math

def inhabitants(month):
    '''
    A village has 25 inhabitants, 
    after each month the number of inhabitants increases by 20% (is multiplied by 1.2)
    and 2 inhabitants disappear
    This function returns the number of inhabitants based on the number of months elapsed.
    PRECONDITIONS: month is a positive integer
    POST CONDITIONS: Inhabitants must be a positive integer
    >>> inhabitants(0)
    25
    >>> inhabitants(1)
    28
    >>> inhabitants(5)
    46
    >>> inhabitants(20)
    533
    '''
    if month == 0:
        return 25
    
    return math.floor(inhabitants(month-1)*1.2-2)

doctest.testmod()
