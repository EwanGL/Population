# coding = utf-8
# auteur = Ewan GRIGNOUX LEVERT
# date = Octobre 2020

import doctest
import math

def inhabitants(month, contamination=0.05):
    '''
    A village has 25 inhabitants, 
    after each month the number of inhabitants increases by 20% (is multiplied by 1.2)
    and 2 inhabitants disappear
    This function returns the number of inhabitants based on the number of months elapsed.
    PRECONDITIONS: month is a positive integer
    POST CONDITIONS: Inhabitants must be a positive integer
    >>> inhabitants(0, 0.05)
    (25, 20)
    >>> inhabitants(1, 0.05)
    (28, 22)
    >>> inhabitants(5, 0.05)
    (46, 30)
    >>> inhabitants(20, 0.05)
    (533, 113)
    '''
    if month == 0:
        return (25,20)
    
    return (math.floor(inhabitants(month-1)[0]*1.2-2), math.floor(inhabitants(month-1)[1]*(1+contamination)))

doctest.testmod()