a = int(input('Prvi broj: '))
b = int(input('Drugi broj: '))

def računanje(a, b):
    try:
        print(f'Zbroj: {a + b}') 
        print(f'Razlika: {a - b}')
        print(f'Umnožak: {a * b}')
        print(f'Količnik: {a / b}')
    except ZeroDivisionError:
        print('Ki kužiš da se sa nulom ne može dijeliti.') 
        print('https://www.youtube.com/watch?v=NKmGVE85GUU')
    

računanje(a, b)
