def ispis(n):
       if n == 1:
              print(1, end=' ')
       else:
              ispis(n-1)
              print(n, end=' ')


n=int(input('Koliko brojeva treba ispisati? '))
ispis(n)
