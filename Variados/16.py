def inverte(s: str) -> str:
    if len(s) <= 1:
        return s
    else:
        return s[-1] + inverte(s[:-1])


print(inverte('carro'))