SUM = '+'
MULT = '*'
OPERS = [SUM, MULT]


# PART 1
def get_results(data, adv=False):
    p_input = [list(row.strip()) for row in data]
    results = []
    for line in p_input:
        numbers = [x for x in line if x != ' ']
        numbers = [int(x) if x.isnumeric() else x for x in numbers]
        numbers = flatten_numbers(numbers, adv)
        print(numbers[0])
        results.append(numbers[0])
    return sum(results)


def flatten_numbers(numbers, adv):
    if '(' not in numbers:
        return [new_math(numbers, adv)]
    else:
        open = 0
        open_ind = None
        close_ind = None
        # find matching parenthesis indexes
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
        before = numbers[:open_ind]
        inside = flatten_numbers(numbers[open_ind+1:close_ind], adv)
        after = numbers[close_ind+1:]
        return flatten_numbers(before + inside + after, adv)


# sum or multiply by order of numbers, not priority
def new_math(numbers, adv):
    if len(numbers) == 1:
        return numbers
    if adv:
        return new_adv_math(numbers)
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
# make all sums first, than all multiplications
def new_adv_math(numbers):
    n = 0
    multipliers = []
    for x in numbers:
        if x == MULT:
            multipliers.append(n)
            n = 0
        elif type(x) == int:
            n += x
    # append last multiplier
    if n > 0:
        multipliers.append(n)
    result = 1
    for x in multipliers:
        result *= x

    return result


def main():
    data = list(open('input.txt', 'r'))
    print('Part ONE')
    print(f'{get_results(data)}')
    print('Part TWO')
    print(f'{get_results(data, True)}')


if __name__ == "__main__":
    main()
