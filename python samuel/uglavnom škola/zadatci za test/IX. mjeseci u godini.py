n_m = int(input('Broj dana u mjesecu: '))

if n_m == 31:
    print('Mjeseci sijačanj, ožujak, svibanj, srpanj, rujan i studeni.')
elif n_m == 30:
    print('Mjeseci travanj, lipanj, kolovoz, listopad i prosinac.')
elif n_m == 29:
    print('Mjesec valjača u prijestupnoj godini.')
elif n_m == 28:
    print('Mjesec veljača.')
else:
    print('Niti jedan mjesec nema toliko dana.')