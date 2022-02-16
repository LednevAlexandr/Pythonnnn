from fractions import Fraction
x=0
y=0
def init(a1,b1,a2,b2):
    global x
    global y
    x=complex(a1,b1)
    y=complex(a2,b2)

def sum():
    return x+y

def multy():
    return x*y

def sub():
    return x-y

def div():
    return x/y

def calk(i):
    return {'+':sum(),'*':multy(),'-':sub(),'/':div()}.get(i,'такого оператора пока что нету')



