# PART 1
def check_sum(numbers, result):
    for i, numb1 in enumerate(numbers):
        for numb2 in numbers[i+1:]:
            if numb1 != numb2 and numb1 + numb2 == result:
                return True
    return False


def check_xmas(data, preamble=25):
    i = preamble
    while i < len(data):
        if not check_sum(data[i-preamble:i], data[i]):
            return data[i]
        i += 1
    return None


# PART 2
def encription_weakness(data, number):
    for i, _ in enumerate(data):
        contiguous = []
        j = i + 1
        while sum(contiguous) < number and j < len(data):
            contiguous = data[i:j]
            if sum(contiguous) == number:
                return min(contiguous) + max(contiguous)
            j += 1
    return None


def main():
    puzzle_input = list(open('input.txt', 'r'))
    data = [int(row.strip()) for row in puzzle_input]
    print('Part ONE')
    wrong_number = check_xmas(data)
    print(f'{wrong_number}')
    print('Part TWO')
    print(f'{encription_weakness(data, wrong_number)}')


if __name__ == "__main__":
    main()
