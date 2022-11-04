
#*----------------------------------------+
#*                   MAP                  | 
#*          map(function, iterables)      |
#*----------------------------------------+
import pandas as pd

def myfunc(n):
    return len(n)

    
x = map(myfunc, ('apple', 'banana', 'cherry'))


def myfunc(a, b):
    return a + b

y = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
