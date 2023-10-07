import random

x, list_, bot = '', [], ''


def igra(x, list_, bot):
    x = input('Kamen, šare, papir: ')
    list_ = ['kamen', 'papir', 'škare']
    bot = random.choice(list_)

    print(bot)

    if x == 'kamen':
        if bot == 'škare':
            print('You win!')
        if bot == 'papir':
            print('Bot wins!')

    if x == 'škare':
        if bot == 'papir':
            print('You win!')
        if bot == 'kamen':
            print('Bot wins!')

    if x == 'papir':
        if bot == 'kamen':
            print('You win!')
        if bot == 'škare':
            print('Bot wins!')

    if x == bot:
        print('Tie!')

    r = input("Rematch[y, n]? ")
    if r == 'y':
        igra(x, list_, bot)


igra(x, list_, bot)
