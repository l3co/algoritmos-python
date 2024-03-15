# Busca Binária

def binary_search(array, item, begin=0, end=None):
    if end is None:
        end = len(array) - 1
    if begin <= end:
        mid = (begin + end) // 2
        if array[mid] == item:
            return mid
        if item < array[mid]:
            return binary_search(array, item, begin, mid - 1)
        else:
            return binary_search(array, item, mid + 1)

    return None


if __name__ == '__main__':
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(binary_search(lista, 10))
