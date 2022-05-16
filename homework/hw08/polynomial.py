from IPython.display import display, Math, Latex
from fractions import Fraction
import numpy as np

def display_poly(poly):
    s = r''
    
    if np.allclose(poly, 0):
        return '$0$'
    
    for i in range(len(poly)):
        if poly[i] != 0:
            # Don't add + if coefficient is negative
            if (isinstance(poly[i], str)) or poly[i] >= 0:
                s += '+'

            # If float version of an int, show as int
            if isinstance(poly[i], float) and poly[i] == int(poly[i]):
                if poly[i] == 1 and i != 0:
                    pass
                elif poly[i] == -1 and i != 0:
                    s += '-'
                else:
                    s += str(int(poly[i]))

            # If decimal, show as rational number
            elif isinstance(poly[i], float):
                f = Fraction(poly[i]).limit_denominator()
                a, b = f.numerator, f.denominator
                if a > 0:
                    s += '\\frac{' + str(a) + '}{' + str(b) + '}'
                else:
                    s += '-\\frac{' + str(-a) + '}{' + str(b) + '}'

            # Otherwise, show normally
            else:
                if poly[i] == 1 and i != 0:
                    pass
                elif poly[i] == -1 and i != 0:
                    s += '-'
                else:
                    s += str(poly[i])

            if i == 0:
                pass
            elif i == 1:
                s += 'x'
            else:
                s += 'x^' + str(i)

    # Remove leading + if it's there
    if s[0] == '+':
        s = s[1:]

#     display(Math(s)) # can uncomment
    return '$' + s + '$'

class Polynomial:

    def __init__(self, coefs):
        self.coefs = np.array(coefs)
        self.deg = len(coefs) - 1

    def __repr__(self):
        return f'Polynomial({self.coefs})'

    def _repr_markdown_(self):
        return display_poly(self.coefs)

    def __iter__(self):
        return iter(self.coefs)

    def as_function(self):
        def f(x):
            return sum([self.coefs[i]*(x**i) for i in range(len(self.coefs))])
        return f
    
    def __add__(self, other):
        return Polynomial(self.coefs + other.coefs)
    
    def __sub__(self, other):
        return Polynomial(self.coefs - other.coefs)