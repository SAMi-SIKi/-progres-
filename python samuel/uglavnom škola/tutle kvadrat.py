from turtle import *

title('Pravokutnik')

st(); lt(90)

a = int(textinput('Duljina', 'a= '))
b = int(textinput('Duljina', 'b= '))

for k in range(2):
       fd(b); rt(90); fd(a); rt(90)
