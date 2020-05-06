def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, s+n)


recurse(1, 0)
# recurse(-1, 0) se passar o n < 0 vai entrar em loop, pois n nunca vai ser == 0 ou  > 0
