SUM = '+'
MULT = '*'
OPERS = [SUM, MULT]


# PART 1
def get_results(data):
    p_input = [list(row.strip()) for row in data]
    results = []
    for line in p_input:
        numbers = [x for x in line if x != ' ']
        numbers = [int(x) if x.isnumeric() else x for x in numbers]
        numbers = flatten_numbers(numbers)
        # print(numbers[0])
        results.append(numbers[0])
    return sum(results)


def flatten_numbers(numbers):
    if '(' not in numbers:
        return [new_math(numbers)]
    else:
        open = 0
        open_ind = None
        close_ind = None
        # get matching parenthesis
        for i, n in enumerate(numbers):
            if n == '(':
                open += 1
                if open_ind is None:
                    open_ind = i
            elif n == ')':
                if open == 1:
                    close_ind = i
                    break
                else:
                    open -= 1
        before_section = numbers[:open_ind]
        section = flatten_numbers(numbers[open_ind+1:close_ind])
        after_section = numbers[close_ind+1:]
        return flatten_numbers(before_section + section + after_section)


def new_math(numbers):
    if len(numbers) == 1:
        return numbers
    n = numbers[0]
    op = numbers[1]
    for x in numbers[2:]:
        if x in OPERS:
            op = x
        else:
            if op == SUM:
                n += x
            elif op == MULT:
                n *= x
    return n


# PART 2
def part_2(data):
    pass


def main():
    data = list(open('input.txt', 'r'))
    print('Part ONE')
    print(f'{get_results(data)}')
    # print('Part TWO')
    # print(f'{part_2(data)}')


if __name__ == "__main__":
    main()
