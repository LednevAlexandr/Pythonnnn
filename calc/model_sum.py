from fractions import Fraction
x = 0
y = 0
def init(a1,b1,a2,b2):
    global x
    global y
    x = Fraction(a1,b1)
    y = Fraction(a2,b2)

def sum():
    return x+y
