def zbroj(n):
       if n == 1:
              return 1
       else:
              return n + zbroj (n-1)


n = int(input('Koliko brojeva treba zbrojiti? '))

print(f'zbroj prvih {n} prirodnih brojeva je {zbroj(n)}')
