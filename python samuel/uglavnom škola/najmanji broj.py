x= int(input('Upiši prvi broj: '))
najmanji= x
while x>0:
       x= int(input('Upiši broj: '))
       if x<najmanji:
              najmanji= x
print(f'Najmanji broj je {najmanji}')