def busca_binaria(list_de_numeros, item):
    baixo = 0
    alto = len(list_de_numeros) - 1

    while baixo <= alto:
        print("==================================================")

        # sum the low and high and divide by 2
        # slip the list in middle
        meio = int((baixo + alto) / 2)

        print(f"Meio: {meio}, Baixo: {baixo}, Alto: {alto}")
        print(f"Meio = (baixo({baixo}) + alto({alto})) / 2 = {meio}")

        chute = list_de_numeros[meio]

        print(
            f'O index correspondente ao meio : list_de_numeros[{meio}] => [{list_de_numeros[meio]}] == {item} = {list_de_numeros[meio] == item}')

        if chute == item:
            return meio, chute
        if chute > item:
            alto = meio - 1
            print(f'alto = {meio} - 1 = {alto}')
        else:
            baixo = meio + 1
            print(f'baixo = {meio} + 1 = {baixo}')
    return None


if __name__ == '__main__':
    minha_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(minha_lista)
    # shuffle(cards)

    seu_numero = int(input('Digite um número a ser adivinhado : '))

    indice, chute = busca_binaria(minha_lista, seu_numero)
    print(f'O chute foi {chute} e foi encontrado no indice {indice}')
