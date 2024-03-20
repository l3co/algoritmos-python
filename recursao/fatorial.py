def factorial(real: int):
    if real == 0:
        return 1
    elif real < 0:
        raise ValueError(f'O fatorial de {real} não é possivel')
    else:
        return real * factorial(real - 1)
