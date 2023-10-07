def ispis(n):
    if n == 1:
        print(1, end=' ')
    else:
        ispis(n-2)
        print(n, end=' ')
    

n = int(input('Do kojeg broja treba ispisati? '))

if n % 1 == 0:
    ispis(n)
else:
    ispis(n-1)