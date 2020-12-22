# PART 1
def memory_game(data, limit):
    numbers = [int(n.strip()) for n in data[0].split(',')][::-1]
    while len(numbers) < limit:
        last_spoken = numbers[0]
        try:
            new_value = numbers.index(last_spoken, 1)
        except ValueError:
            new_value = 0
        numbers.insert(0, new_value)

    # Message to verify solution if available
    message = None
    if len(data) > 1:
        message = f'SHOULD BE {data[1]}'

    return f'{numbers[0]} {message}'


# PART 2 (same result as part 1, just more efficient)
def memory_game_v2(data, limit):
    numbers_tmp = [int(n.strip()) for n in data[0].split(',')]
    numbers = {}
    # write all except last numbers in dictionary with index as value
    for i, n in enumerate(numbers_tmp[:-1]):
        numbers[n] = i
    last_spoken = numbers_tmp[-1]
    ctr = len(numbers)
    while ctr < limit-1:
        try:
            previous = ctr - numbers[last_spoken]
            numbers[last_spoken] = ctr
            last_spoken = previous
        except KeyError:
            numbers[last_spoken] = ctr
            last_spoken = 0
        ctr += 1

    # Message to verify solution if available
    message = None
    if len(data) > 1:
        message = f'SHOULD BE {data[2]}'

    return f'{last_spoken} {message}'


def main():
    data = list(open('input.txt', 'r'))
    print('Part ONE')
    print(f'{memory_game(data, 2020)}')
    print('Part TWO')
    print(f'{memory_game_v2(data, 30000000)}')


if __name__ == "__main__":
    main()
