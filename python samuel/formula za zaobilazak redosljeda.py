def func(**xy):
    ans = xy['a'] + xy['b'] * xy['c'] * xy['d']  # <--formula za računalje
    print(ans)
    return


# npr. brojevi
func(a=1, b=4, c=2, d=1)
