def ispis(n):
       if n == 1:
              print(1, end=' ')
       else:
              print(n, end=' ')
              ispis(n-1)


n=int(input('Koliko brojeva treba ispisati? '))
ispis(n)
