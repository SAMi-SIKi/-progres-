k = int(input('Troznamenkasti brojevi djeljivi s:'))
x = 100

try:
       while x % k != 0:
              x += 1
       for broj in range(x, 1000, k):
              print(broj, end=', ')
except ZeroDivisionError:
       print('Nemože se dijeliti s nulom.')
       print('https://www.youtube.com/watch?v=NKmGVE85GUU')
