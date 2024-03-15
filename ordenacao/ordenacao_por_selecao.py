def busca_menor(arr):
    menor = arr[0]
    menor_index = 0

    """
    Todas as vezes que o menor elemento for encontrado este sera adicionado em uma nova lista e
    e também sera removido da anterior até que chegue o ponto de não haver mais elementos na lista
    """

    print(f"Arrays => ", arr)

    for i in range(1, len(arr)):
        if arr[i] < menor:
            menor = arr[i]
            menor_index = i

    return menor_index


def ordenacao_por_selecao(arr):
    novo_arr = []
    for i in range(len(arr)):
        menor = busca_menor(arr)
        novo_arr.append(arr.pop(menor))

        print(f"Novo Array => {novo_arr}")

    return novo_arr


if __name__ == '__main__':
    print(ordenacao_por_selecao([1, 23, 5, 32, 8, 5, 7]))
