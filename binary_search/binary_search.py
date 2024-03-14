def binary_search(card_list, item):
    low = 0
    high = len(card_list) - 1

    while low <= high:
        print("==================================================")

        # sum the low and high and divide by 2
        # slip the list in middle
        middle = int((low + high) / 2)
        print(f"middle = (low({low}) + high({high})) / 2 = {middle}")
        guess = card_list[middle]
        print(f'guessed is card[{middle}] => [{card_list[middle]}] == {item} = {card_list[middle] == item}')

        if guess == item:
            return middle
        if guess > item:
            high = middle - 1
            print(f'high = {middle} - 1 = {high}')
        else:
            low = middle + 1
            print(f'low = {middle} + 1 = {low}')
    return None


if __name__ == '__main__':
    cards = list(range(1, 100))
    print(cards)
    number_to_guessed = int(input('I guess a number : '))
    print(binary_search(cards, number_to_guessed))
