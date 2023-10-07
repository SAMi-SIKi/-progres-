x= int(input('Upiši prvi broj: '))
najveći= x
while x>0:
       x= int(input('Upiši broj: '))
       if x>najveći:
              najveći= x
print(f'Najveći broj je {najveći}')