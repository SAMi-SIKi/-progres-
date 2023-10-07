from turtle import *
from time import *

title("Kocka")
ht()


def setup1():
    penup()
    lt(180)
    fd(100)
    rt(180)
    pendown()


def stranica():
    for k in range(4):
        fd(130)
        lt(90)


def crte1():
    lt(45)
    for k in range(5):
        pendown()
        fd(6.5)
        penup()
        fd(6.5)
    lt(45)
    for k in range(10):
        pendown()
        fd(6.5)
        penup()
        fd(6.5)
        pendown()
    lt(135)
    fd(65)


def setup2():
    rt(180)
    fd(65)
    rt(45)


def crte2():
    fd(130)
    rt(135)
    fd(65)
    lt(180)
    fd(65)
    rt(135)
    fd(130)
    rt(45)
    fd(65)


def setup3():
    rt(180)
    fd(65)
    lt(135)


def crte3():
    for k in range(10):
        pendown()
        fd(6.5)
        penup()
        fd(6.5)
        pendown()
    rt(180)


def main():
    setup1()
    stranica()
    crte1()
    setup2()
    crte2()
    setup3()
    crte3()


main()
sleep(5)
