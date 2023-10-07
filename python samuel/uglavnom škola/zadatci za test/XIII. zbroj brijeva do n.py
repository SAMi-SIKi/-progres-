n = int(input('Do oje će se broja zbrajati? '))

def zbroj(n):
       if n == 1:
              return 1
       else:
              return n + zbroj(n-1)


print(f'Zbroj prvih {n} prirodnih brojeva je {zbroj(n)}')
