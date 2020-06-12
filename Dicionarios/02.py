def print_hist(h):
    for c in h:
        print(c, h[c])

    for key in sorted(h):
        print(key, h[key])


print_hist({'a': 1, 'b': 2, 'c': 3})
