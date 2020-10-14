# coding = utf-8
# auteur = Ewan GRIGNOUX LEVERT
# date = Octobre 2020

import doctest
import math

def inhabitants(month, contamination=0.5):
    '''
    A village has 25 inhabitants, 
    after each month the number of inhabitants increases by 20% (is multiplied by 1.2)
    and 2 inhabitants disappear
    This function returns the number of inhabitants based on the number of months elapsed.
    PRECONDITIONS: month is a positive integer
    POST CONDITIONS: Inhabitants must be a positive integer
    >>> inhabitants(0)
    (25, 1, 0)
    >>> inhabitants(1)
    (28, 2, 0)
    >>> inhabitants(5)
    (46, 32, 1)
    >>> inhabitants(20)
    (-39266, 794244, 30364)
    '''
    if month == 0:
        return (25,1,0)
    
    h, i, d = inhabitants(month-1)

    return (math.floor(h * 1.2 - 2 - d), math.floor(i*2-d), math.floor(0.75*i*0.02))
doctest.testmod()
