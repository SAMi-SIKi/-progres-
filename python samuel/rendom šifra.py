import random

u = input('Želišli velika slova u šifri?[Y/N] ')
l = input('Želišli mala slova u šifri?[Y/N] ')
n = input('Želišli brjeve u šifri?[Y/N] ')
lenght = int(input('Koliko dugu šifru želiš? '))

low_alfList = 'qaywsxedcrftgbzhnujmikolp'
up_alfList = 'QAYWSXEDCRFVTGBZHNUJMIKOLPČŠĆĐŽ'
numList = '123456789'
script = ''

if u == 'Y':
    script += up_alfList
if l == 'Y':
    script += low_alfList
if n == 'Y':
    script += numList

pasword = ''.join(random.sample(script, lenght))

if pasword != '':
    print(f'Tvoja šifra je: {pasword}')
if pasword == '':
    print(f'Pa želiš lišifru ili ne?')