k = int(input('Dvoznamenkasti brojevi djeljivi s: '))
x = 10

try:
       while x % k != 0:
              x += 1
       for broj in range(x, 100, k):
              print(broj, end=' ')
except ZeroDivisionError:
       print('Nemože se dijeliti s nulom.')
       print('https://www.youtube.com/watch?v=NKmGVE85GUU')