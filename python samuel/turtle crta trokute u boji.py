from turtle import *
from random import *

penup()
lt(180)
fd(350)
rt(270)
pendown()


def rendboje():
    r = randrange(0, 256)
    g = randrange(0, 256)
    b = randrange(0, 256)
    color(r, g, b)


def trokut(t):
    rendboje()
    begin_fill()
    for x in range(4):
        fd(t)
        lt(120)
    end_fill()


def niz_trokuta(n, t):
    if n == 1:
        trokut(t)
    else:
        trokut(t)
        rt(120)
        niz_trokuta(n-1, t)


title('!!! NAJBOLJI NIZ ŠARENIH KVADRATA KOJE STE IKADA VIDJELI U ŽIVOTU !!!')
lt(90)
colormode(255)
t = textinput('Stranica', 't=')
n = textinput('Broj trokuta', 'n=')
t = int(t)
n = int(n)
niz_trokuta(n, t)
