from decimal import Decimal
import math

def rounding(n):
    print(round(n, 2))
    print(format(n, '.2f'))
    print(Decimal(n))
    print(math.floor(n))
    print(math.ceil(n))

"""This is a docstring."""
"""Is this a docstring? yes"""

rounding(2.3456)
rounding(-3.434)
